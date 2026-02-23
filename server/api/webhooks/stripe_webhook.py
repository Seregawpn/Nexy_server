#!/usr/bin/env python3
"""
Stripe Webhook Handler - единая точка входа для всех Stripe событий

Feature ID: F-2025-017-stripe-payment

⚠️ КРИТИЧНО:
- Idempotency через UNIQUE(stripe_event_id)
- Event-идемпотентность + out-of-order guard на уровне repository
- Cache invalidation после обработки
"""
import logging
import json
from typing import Dict, Any, Optional
from datetime import datetime, timezone
from aiohttp import web

try:
    import stripe as stripe_lib
except ImportError:  # pragma: no cover - optional dependency
    stripe_lib = None

logger = logging.getLogger(__name__)

from modules.subscription.core.subscription_types import map_stripe_status_to_local_status

TERMINAL_SUCCESS_STATUSES = {
    "processed",
    "subscription_synced",
    "ignored",
    "duplicate",
}

RETRYABLE_STATUSES = {
    "error",
    "skipped",
}


async def stripe_webhook_handler(request: web.Request) -> web.Response:
    """
    POST /webhook/stripe
    
    Обрабатывает webhook события от Stripe.
    
    ⚠️ КРИТИЧНО:
    1. Verify signature
    2. Process event with idempotency in repository
    3. Invalidate cache after terminal handling
    4. Return 5xx for retryable failures
    """
    from config.unified_config import get_config
    from modules.subscription import get_subscription_module
    
    config = get_config().subscription
    
    # Проверка, что модуль включен
    if not config.is_active():
        logger.debug("[F-2025-017] Webhook received but subscription disabled")
        return web.json_response({'status': 'disabled'}, status=200)
    
    try:
        # Получаем payload
        payload = await request.read()
        sig_header = request.headers.get('Stripe-Signature', '')
        
        logger.debug(f"[F-2025-017] Webhook received: payload_size={len(payload)}, sig_header={bool(sig_header)}")
        
        # Verify signature
        event = await _verify_and_construct_event(
            payload=payload,
            sig_header=sig_header,
            webhook_secret=config.stripe_webhook_secret
        )
        
        if event is None:
            logger.warning("[F-2025-017] Invalid webhook signature")
            return web.json_response({'error': 'Invalid signature'}, status=400)
        
        event_id = event.get('id', 'unknown')
        event_type = event.get('type', 'unknown')
        
        logger.info(f"[F-2025-017] Webhook received: type={event_type} id={event_id}")
        
        # Process event
        try:
            result = await _process_event(event)
            result_status = str(result.get("status", "")).strip().lower()
            if result_status in RETRYABLE_STATUSES:
                raise RuntimeError(f"retryable_result:{result_status}:{result.get('reason', 'unknown')}")
            if result_status not in TERMINAL_SUCCESS_STATUSES:
                raise RuntimeError(f"unknown_result_status:{result_status or 'empty'}")
            
            # Invalidate cache
            try:
                subscription_module = get_subscription_module()
                if subscription_module:
                    subscription_module.invalidate_all_cache()
            except Exception as e:
                logger.warning(f"[F-2025-017] Cache invalidation failed: {e}")
            
            logger.info(f"[F-2025-017] Webhook processed: type={event_type} id={event_id} result={result}")
            
            if result_status == "duplicate":
                return web.json_response({
                    'status': 'duplicate',
                    'event_id': event_id,
                    'result': result,
                }, status=200)

            # Return 200 OK for terminal-success events (including ignored)
            return web.json_response({
                'status': 'processed',
                'event_id': event_id,
                'result': result
            }, status=200)
        except Exception as e:
            import traceback
            logger.error(f"[F-2025-017] Event processing exception: {e}")
            logger.error(f"[F-2025-017] Traceback: {traceback.format_exc()}")
            # Return 5xx to allow Stripe retry on transient/internal processing errors.
            return web.json_response({
                'status': 'error',
                'event_id': event_id,
                'message': str(e)
            }, status=500)
        
    except json.JSONDecodeError:
        logger.error("[F-2025-017] Invalid JSON in webhook payload")
        return web.json_response({'error': 'Invalid JSON'}, status=400)
        
    except Exception as e:
        import traceback
        logger.error(f"[F-2025-017] Webhook error: {e}")
        logger.error(f"[F-2025-017] Traceback: {traceback.format_exc()}")
        return web.json_response({
            'status': 'error',
            'message': str(e)
        }, status=500)


async def _verify_and_construct_event(
    payload: bytes,
    sig_header: str,
    webhook_secret: str
) -> Optional[Dict[str, Any]]:
    """
    Verify Stripe signature and construct event.
    
    Returns:
        Event dict if valid, None otherwise
    """
    try:
        if not webhook_secret:
            # В dev режиме без secret принимаем как есть
            logger.warning("[F-2025-017] No webhook secret configured - accepting without verification")
            return json.loads(payload)

        if stripe_lib is None:
            logger.error("[F-2025-017] stripe library not installed")
            return None

        event = stripe_lib.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
        return dict(event)

    except Exception as e:
        if stripe_lib and isinstance(e, stripe_lib.error.SignatureVerificationError):
            logger.error(f"[F-2025-017] Signature verification failed: {e}")
            return None
        logger.error(f"[F-2025-017] Event construction failed: {e}")
        return None


async def _check_idempotency(event_id: str) -> bool:
    """
    Legacy compatibility wrapper.
    Idempotency owner path is record_event() in _process_event.
    """
    try:
        from modules.subscription.repository.subscription_repository import SubscriptionRepository
        repo = SubscriptionRepository()
        return repo.event_exists(event_id, processed_only=True)
    except Exception as e:
        logger.error(f"[F-2025-017] Idempotency check failed: {e}")
        return False


async def _process_event(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process Stripe event.
    
    ⚠️ КРИТИЧНО: Идемпотентность через record_event + guards в repository
    
    Returns:
        Processing result
    """
    from modules.subscription.repository.subscription_repository import SubscriptionRepository
    event_id = event.get('id')
    event_type = event.get('type')
    event_data = event.get('data', {}).get('object', {})
    stripe_created = event.get('created')
    stripe_event_at = datetime.fromtimestamp(stripe_created, tz=timezone.utc) if stripe_created else datetime.now(timezone.utc)

    if not isinstance(event_id, str) or not event_id:
        return {'status': 'error', 'message': 'missing_event_id'}
    if not isinstance(event_type, str) or not event_type:
        return {'status': 'error', 'message': 'missing_event_type'}
    
    repo = SubscriptionRepository()
    
    # Extract hardware_id from metadata, then fallback to local DB linkage.
    hardware_id = _extract_hardware_id(event_data)
    if not hardware_id:
        hardware_id = _resolve_hardware_id_from_repo(event_data, repo)
    
    try:
        # Record event first (for idempotency)
        recorded = repo.record_event(
            stripe_event_id=event_id,
            event_type=event_type,
            hardware_id=hardware_id,
            event_data=event_data,
            stripe_created_at=stripe_created,
            processed=False  # Mark as processing
        )
        
        if not recorded:
            return {'status': 'duplicate', 'reason': 'already_recorded'}
        
        # Process based on event type
        # Pass event_id AND stripe_created for idempotency/ordering guards
        result = await _handle_event_type(
            event_type, 
            event_data, 
            hardware_id, 
            repo,
            event_id,
            stripe_event_at
        )

        result_status = str(result.get("status", "")).strip().lower()
        if result_status in TERMINAL_SUCCESS_STATUSES:
            # Mark as processed only for terminal outcomes.
            repo.record_event(
                stripe_event_id=event_id,
                event_type=event_type,
                hardware_id=hardware_id,
                event_data=event_data,
                stripe_created_at=stripe_created,
                processed=True
            )

        return result
        
    except Exception as e:
        import traceback
        logger.error(f"[F-2025-017] Event processing failed: {e}")
        logger.error(f"[F-2025-017] Traceback: {traceback.format_exc()}")
        return {'status': 'error', 'reason': 'processing_exception', 'message': str(e)}


def _extract_hardware_id(event_data: Dict[str, Any]) -> Optional[str]:
    """Extract hardware_id from event metadata"""
    # Try metadata first
    metadata = event_data.get('metadata', {})
    if 'hardware_id' in metadata:
        return metadata['hardware_id']
    
    # Try client_reference_id (for checkout sessions)
    if 'client_reference_id' in event_data:
        return event_data['client_reference_id']
    
    # Try customer metadata
    customer = event_data.get('customer')
    if isinstance(customer, dict):
        customer_metadata = customer.get('metadata', {})
        if 'hardware_id' in customer_metadata:
            return customer_metadata['hardware_id']
    
    return None


def _resolve_hardware_id_from_repo(event_data: Dict[str, Any], repo) -> Optional[str]:
    """
    Fallback resolver for events where Stripe object lacks direct hardware_id metadata
    (e.g., invoice.* events).
    Resolution order:
    1) subscriptions.stripe_subscription_id
    2) subscriptions.stripe_customer_id
    """
    # invoice.subscription is usually a string id, but keep dict-safe parsing
    subscription_ref = event_data.get('subscription')
    if isinstance(subscription_ref, str) and subscription_ref:
        sub = repo.get_subscription_by_stripe_subscription_id(subscription_ref)
        if sub and sub.get('hardware_id'):
            return sub.get('hardware_id')
    elif isinstance(subscription_ref, dict):
        sub_id = subscription_ref.get('id')
        if sub_id:
            sub = repo.get_subscription_by_stripe_subscription_id(sub_id)
            if sub and sub.get('hardware_id'):
                return sub.get('hardware_id')

    customer_ref = event_data.get('customer')
    if isinstance(customer_ref, str) and customer_ref:
        sub = repo.get_subscription_by_stripe_customer_id(customer_ref)
        if sub and sub.get('hardware_id'):
            return sub.get('hardware_id')
    elif isinstance(customer_ref, dict):
        customer_id = customer_ref.get('id')
        if customer_id:
            sub = repo.get_subscription_by_stripe_customer_id(customer_id)
            if sub and sub.get('hardware_id'):
                return sub.get('hardware_id')

    return None


async def _handle_event_type(
    event_type: str,
    event_data: Dict[str, Any],
    hardware_id: Optional[str],
    repo,
    event_id: str,
    stripe_created: Optional[datetime]
) -> Dict[str, Any]:
    """
    Handle specific event types.
    
    Supported events:
    - checkout.session.completed
    - customer.subscription.updated
    - customer.subscription.deleted
    - invoice.payment_succeeded
    - invoice.payment_failed
    - invoice.payment_action_required
    """
    if not hardware_id:
        logger.warning(f"[F-2025-017] No hardware_id for event {event_type}")
        return {'status': 'skipped', 'reason': 'no_hardware_id'}
    
    from modules.subscription.core.state_machine import SubscriptionStateMachine
    
    subscription = repo.get_subscription(hardware_id)
    current_status = subscription.get('status') if subscription else None
    
    # Initialize variables (will be set for handled events)
    new_status = None
    stripe_status = None
    
    if event_type == 'checkout.session.completed':
        # Centralized fallback sync in SubscriptionModule (single owner mapping path)
        try:
            from modules.subscription import get_subscription_module
            subscription_module = get_subscription_module()
            if subscription_module:
                session_id = event_data.get('id')
                if session_id:
                    result = await subscription_module.reconcile_checkout_success(session_id)
                    if result.get("ok"):
                        return {'status': 'subscription_synced', 'success': True, 'result': result}
                    return {
                        'status': 'skipped',
                        'success': False,
                        'reason': 'reconcile_not_ok',
                        'result': result,
                    }
        except Exception as e:
            logger.warning(f"[F-2025-017] checkout.session.completed reconcile fallback failed: {e}")
        return {'status': 'skipped', 'success': False, 'reason': 'reconcile_unavailable'}

    
    elif event_type == 'invoice.payment_succeeded':
        stripe_status = 'active'
        new_status = map_stripe_status_to_local_status(stripe_status, current_status)
        
    elif event_type == 'invoice.payment_failed':
        stripe_status = 'past_due'
        new_status = map_stripe_status_to_local_status(stripe_status, current_status)
        
    elif event_type == 'customer.subscription.updated':
        stripe_status = event_data.get('status', 'active')
        cancel_at_period_end = bool(event_data.get('cancel_at_period_end', False))
        cancel_at = event_data.get('cancel_at')
        cancel_scheduled = cancel_at_period_end or bool(cancel_at)
        new_status = map_stripe_status_to_local_status(stripe_status, current_status)
            
    elif event_type == 'customer.subscription.deleted':
        stripe_status = 'deleted'
        new_status = map_stripe_status_to_local_status(stripe_status, current_status)
        
    else:
        # Unhandled event types (payment_intent.*, charge.*, etc.)
        # These are informational and don't require state changes
        logger.debug(f"[F-2025-017] Unhandled event type: {event_type} - ignoring")
        return {'status': 'ignored', 'reason': 'unhandled_event_type'}
    
    # Use state machine for transition (only for handled events)
    if new_status is None or stripe_status is None:
        logger.warning(f"[F-2025-017] Missing status for event {event_type}")
        return {'status': 'error', 'reason': 'missing_status'}
    
    result = SubscriptionStateMachine.transition(
        hardware_id=hardware_id,
        from_status=current_status,
        to_status=new_status,
        event_type=event_type,
        repository=repo,
        stripe_status=stripe_status,
        stripe_event_id=event_id,          # CORRECT: event_id (evt_...) not object id
        stripe_event_at=stripe_created,    # CORRECT: timestamp from event
        current_period_end=event_data.get('current_period_end'),
        cancel_at_period_end=cancel_scheduled if event_type == 'customer.subscription.updated' else None,
    )
    
    if result.get("success"):
        return {
            "status": "processed",
            "success": True,
            "reason": "state_transition_applied",
            "result": result,
        }
    return {
        "status": "error",
        "success": False,
        "reason": "state_transition_failed",
        "result": result,
    }


# Factory function for route registration
def get_webhook_routes() -> list:
    """Get webhook routes for aiohttp app"""
    return [
        web.post('/webhook/stripe', stripe_webhook_handler)
    ]
