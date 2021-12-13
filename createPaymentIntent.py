import sys
import logging
import json
import stripe
import os


def lambda_handler(data, context):
  email = data['email']
  payment_method_id = data['payment_method_id']
  
  stripe.api_key = 'pk_test_51IYZ9kBacowHdHsgZqK8SpJeHum3mmXSupwIbZ4693MSMmGlgsqur6BrkhtdGCHq78SSeF5o73wrIxXcavr8rAKw00BHnxQmqm' #Your test/live secret key
  
  payment_intent = stripe.PaymentIntent.create(
    payment_method_types=['card'],
    payment_method = payment_method_id,
    amount=1000,
    application_fee_amount=140,
    currency='eur',
    stripe_account='acct_1K5qyBPjANuxJ0xT',#connected account ID
    receipt_email=email,
    confirm=True
  )
  
  return payment_intent.client_secret
