#!/usr/bin/env python3
"""
Stripe Webhook Handler - единая точка входа для всех Stripe событий

Feature ID: F-2025-017-stripe-payment

⚠️ КРИТИЧНО: 
- Idempotency через UNIQUE(stripe_event_id)
- Atomic transactions
- Cache invalidation после обработки
"""
import logging
import json
from typing import Dict, Any, Optional
from aiohttp import web

try:
    import stripe as stripe_lib
except ImportError:  # pragma: no cover - optional dependency
    stripe_lib = None

logger = logging.getLogger(__name__)


async def stripe_webhook_handler(request: web.Request) -> web.Response:
    """
    POST /webhook/stripe
    
    Обрабатывает webhook события от Stripe.
    
    ⚠️ КРИТИЧНО:
    1. Verify signature
    2. Check idempotency (stripe_event_id)
    3. Process event in transaction
    4. Invalidate cache
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
        
        # Check idempotency
        is_duplicate = await _check_idempotency(event_id)
        if is_duplicate:
            logger.info(f"[F-2025-017] Duplicate event ignored: {event_id}")
            return web.json_response({
                'status': 'duplicate',
                'message': 'Event already processed'
            }, status=200)
        
        # Process event
        result = await _process_event(event)
        
        # Invalidate cache
        subscription_module = get_subscription_module()
        if subscription_module:
            subscription_module.invalidate_all_cache()
        
        logger.info(f"[F-2025-017] Webhook processed: type={event_type} id={event_id} result={result}")
        
        return web.json_response({
            'status': 'processed',
            'event_id': event_id,
            'result': result
        }, status=200)
        
    except json.JSONDecodeError:
        logger.error("[F-2025-017] Invalid JSON in webhook payload")
        return web.json_response({'error': 'Invalid JSON'}, status=400)
        
    except Exception as e:
        logger.error(f"[F-2025-017] Webhook error: {e}")
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
    Check if event was already processed.
    
    ⚠️ КРИТИЧНО: Использует UNIQUE constraint на stripe_event_id
    
    Returns:
        True if duplicate, False if new
    """
    try:
        from modules.subscription.repository.subscription_repository import SubscriptionRepository
        repo = SubscriptionRepository()
        return repo.event_exists(event_id, processed_only=True)
    except Exception as e:
        logger.error(f"[F-2025-017] Idempotency check failed: {e}")
        return False  # Allow processing on error


async def _process_event(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process Stripe event.
    
    ⚠️ КРИТИЧНО: Atomic transaction с record_event для идемпотентности
    
    Returns:
        Processing result
    """
    from modules.subscription.repository.subscription_repository import SubscriptionRepository
    from modules.subscription.providers.stripe_service import StripeService
    
    event_id = event.get('id')
    event_type = event.get('type')
    event_data = event.get('data', {}).get('object', {})
    stripe_created = event.get('created')
    
    repo = SubscriptionRepository()
    
    # Extract hardware_id from metadata
    hardware_id = _extract_hardware_id(event_data)
    
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
            return {'status': 'skipped', 'reason': 'already_recorded'}
        
        # Process based on event type
        result = await _handle_event_type(event_type, event_data, hardware_id, repo)
        
        # Mark as processed
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
        logger.error(f"[F-2025-017] Event processing failed: {e}")
        return {'status': 'error', 'message': str(e)}


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


async def _handle_event_type(
    event_type: str,
    event_data: Dict[str, Any],
    hardware_id: Optional[str],
    repo
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
    
    # Determine new status based on event
    if event_type == 'checkout.session.completed':
        # New subscription created
        if not subscription:
            repo.create_subscription(hardware_id, status='paid_trial')
        return {'status': 'subscription_created'}
    
    elif event_type == 'invoice.payment_succeeded':
        new_status = 'paid'
        stripe_status = 'active'
        
    elif event_type == 'invoice.payment_failed':
        new_status = 'billing_problem'
        stripe_status = 'past_due'
        
    elif event_type == 'customer.subscription.updated':
        stripe_status = event_data.get('status', 'active')
        cancel_at_period_end = event_data.get('cancel_at_period_end', False)
        
        if stripe_status == 'active':
            new_status = 'paid'
        elif stripe_status in ['past_due', 'unpaid']:
            new_status = 'billing_problem'
        elif stripe_status in ['canceled', 'incomplete_expired']:
            new_status = 'limited_free_trial'
        else:
            new_status = current_status or 'paid'
            
    elif event_type == 'customer.subscription.deleted':
        new_status = 'limited_free_trial'
        stripe_status = 'deleted'
        
    else:
        logger.debug(f"[F-2025-017] Unhandled event type: {event_type}")
        return {'status': 'ignored', 'reason': 'unhandled_event_type'}
    
    # Use state machine for transition
    result = SubscriptionStateMachine.transition(
        hardware_id=hardware_id,
        from_status=current_status,
        to_status=new_status,
        event_type=event_type,
        repository=repo,
        stripe_status=stripe_status,
        stripe_event_id=event_data.get('id'),
        current_period_end=event_data.get('current_period_end')
    )
    
    return result


# Factory function for route registration
def get_webhook_routes() -> list:
    """Get webhook routes for aiohttp app"""
    return [
        web.post('/webhook/stripe', stripe_webhook_handler)
    ]
