#!/usr/bin/env python3
"""
Migration Script: Populate stripe_customer_id for existing subscriptions

This script queries Stripe for all customers with hardware_id in metadata
and updates the local DB with the stripe_customer_id.

Run from server directory:
    python -m scripts.migrate_stripe_customer_ids

Feature ID: F-2025-017-stripe-payment
"""
import os
import sys
import logging
from dotenv import load_dotenv

# Setup path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def migrate_stripe_customer_ids():
    """
    Migrate stripe_customer_id from Stripe to local DB.
    
    Algorithm:
    1. Get all subscriptions from DB where stripe_customer_id is NULL
    2. For each, search Stripe customers by metadata.hardware_id
    3. If found, update local DB with stripe_customer_id
    """
    import stripe
    from modules.subscription.repository.subscription_repository import SubscriptionRepository
    from config.unified_config import get_config
    
    # Initialize Stripe
    stripe_key = get_config().subscription.stripe_secret_key
    if not stripe_key:
        logger.error("Stripe API key not configured for active mode")
        return
    
    stripe.api_key = stripe_key
    repo = SubscriptionRepository()
    
    # Get all subscriptions without stripe_customer_id
    conn = repo._get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT hardware_id, status, email 
                FROM subscriptions 
                WHERE stripe_customer_id IS NULL OR stripe_customer_id = ''
            """)
            subscriptions = cur.fetchall()
    finally:
        conn.close()
    
    logger.info(f"Found {len(subscriptions)} subscriptions without stripe_customer_id")
    
    if not subscriptions:
        logger.info("No subscriptions to migrate")
        return
    
    # Build hardware_id set for lookup
    hardware_ids = {row[0]: {'status': row[1], 'email': row[2]} for row in subscriptions}
    
    # Fetch all Stripe customers and match by metadata
    updated = 0
    errors = 0
    
    logger.info("Fetching customers from Stripe...")
    
    try:
        # List all customers (paginated)
        customers = stripe.Customer.list(limit=100)
        
        for customer in customers.auto_paging_iter():
            # Safely access metadata
            metadata = getattr(customer, 'metadata', {}) or {}
            if isinstance(customer, dict): # Handle if it's a dict
                metadata = customer.get('metadata', {}) or {}
                
            hw_id = metadata.get('hardware_id')
            
            if hw_id and hw_id in hardware_ids:
                # Found a match! Update local DB
                try:
                    # Safely get customer ID
                    cust_id = customer.id if hasattr(customer, 'id') else customer.get('id')
                    
                    # Safely get subscription ID
                    sub_id = None
                    subscriptions = getattr(customer, 'subscriptions', None)
                    if not subscriptions and isinstance(customer, dict):
                        subscriptions = customer.get('subscriptions')
                        
                    if subscriptions:
                        # Check if data exists and list is not empty
                        data_list = getattr(subscriptions, 'data', [])
                        if isinstance(subscriptions, dict):
                             data_list = subscriptions.get('data', [])
                             
                        if data_list and len(data_list) > 0:
                            first_sub = data_list[0]
                            sub_id = first_sub.id if hasattr(first_sub, 'id') else first_sub.get('id')
                    
                    repo.update_stripe_ids(
                        hardware_id=hw_id,
                        customer_id=cust_id,
                        subscription_id=sub_id
                    )
                    logger.info(f"✅ Updated {hw_id[:8]}... -> customer={cust_id}")
                    updated += 1
                    
                    # Remove from set to track unmatched
                    if hw_id in hardware_ids:
                        del hardware_ids[hw_id]
                    
                except Exception as e:
                    logger.error(f"❌ Failed to update {hw_id[:8]}...: {e}")
                    import traceback
                    logger.error(traceback.format_exc())
                    errors += 1
                    
    except stripe.error.StripeError as e:
        logger.error(f"Stripe API error: {e}")
        return
    
    # Summary
    logger.info("=" * 50)
    logger.info(f"Migration complete:")
    logger.info(f"  ✅ Updated: {updated}")
    logger.info(f"  ❌ Errors: {errors}")
    logger.info(f"  ⚠️  Unmatched (no Stripe customer): {len(hardware_ids)}")
    
    if hardware_ids:
        logger.info("\nUnmatched hardware_ids (need manual review):")
        for hw_id in list(hardware_ids.keys())[:10]:
            logger.info(f"  - {hw_id[:16]}...")


if __name__ == "__main__":
    print("=" * 50)
    print("Stripe Customer ID Migration")
    print("=" * 50)
    print()
    
    confirm = input("This will update your database. Continue? [y/N]: ")
    if confirm.lower() != 'y':
        print("Aborted.")
        sys.exit(0)
    
    migrate_stripe_customer_ids()
