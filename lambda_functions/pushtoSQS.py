import json
import boto3
import re
import random

sqs = boto3.client('sqs')
QUEUE_URL = 'https://sqs.us-east-2.amazonaws.com/011528301997/shippingQueue'

def isValidCard(number):
    """Validate a fake credit card number (16 digits)."""
    return bool(re.match(r'^[0-9]{16}$', number))

def generateProductID():
    """Generate a random 7-digit product ID."""
    return str(random.randint(1000000, 9999999))

def lambda_handler(event, context):
    try:
        print("Incoming event:", event)  
        # handles both http and rest api requests
        body = event.get("body")
        if isinstance(body, str):
            body = json.loads(body)
        elif isinstance(body, dict):
            pass  
        else:
            body = event

        print("Parsed body:", body)

        required_fields = ['name', 'address', 'email', 'product', 'credit_card', 'exp', 'cvv']
        for field in required_fields:
            if field not in body:
                print(f"Missing field: {field}")
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': f'Missing required field: {field}'})
                }


        cardNumber = body['credit_card']
        if not isValidCard(cardNumber):
            print("Invalid card number:", cardNumber)
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid Card Number'})
            }

        body['productID'] = generateProductID()
        print("Generated product ID:", body['productID'])

        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(body)
        )
        print("SQS response:", response)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Order placed successfully',
                'product_id': body['productID']
            })
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
