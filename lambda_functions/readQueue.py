import json
import boto3

ses = boto3.client('ses', region_name='us-east-2')
SENDER = "khanhamza2293@gmail.com"

def lambda_handler(event, context): 
    print("=== Lambda #2 started ===")
    print("Incoming event:", json.dumps(event))
    
    for record in event['Records']:
        message = json.loads(record['body'])
        email = message['email']
        name = message['name']
        address = message['address']
        product = message['product']
        product_id = message['productID']

        if not email:
            print("No email provided in message, skipping.")
            continue

        subject = 'Shipping Confirmation'
        body = (
            f"Hi {name},\n\n"
            f"Your order for {product} has been shipped to:\n"
            f"{address}\n\n"
            f"Product ID: {product_id}\n\n"
            f"Thank you for shopping with us!\n\n"

        )

        try:
            ses.send_email(
                Source=SENDER,
                Destination={'ToAddresses': [email]},
                Message={
                    'Subject': {'Data': subject},
                    'Body': {'Text': {'Data': body}}
                }
            )
            print(f"Email sent to {email}")
        except Exception as e:
            print(f"Error sending email to {email}: {str(e)}")
    return {
        'statusCode': 200,
    }
