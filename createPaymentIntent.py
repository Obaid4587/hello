import sys
import logging
import json
import stripe
import os


def lambda_handler(data, context):
  email = data['email']
  payment_method_id = data['payment_method_id']
  
  stripe.api_key = 'sk_test_...' #Your test/live secret key
  
  payment_intent = stripe.PaymentIntent.create(
    payment_method_types=['card'],
    payment_method = payment_method_id,
    amount=1000,
    application_fee_amount=140,
    currency='eur',
    stripe_account='acct_1G...',#connected account ID
    receipt_email=email,
    confirm=True
  )
  
  return payment_intent.client_secret
