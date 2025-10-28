# AWS Shipping Form Mini Project 🚀

A small serverless web app that collects shipping info, validates fake credit cards, queues data in SQS, and sends confirmation emails using AWS SES.

## 🧩 Architecture

Frontend → API Gateway → Lambda #1 → SQS → Lambda #2 → SES → Email

## ⚙️ Technologies Used
- AWS Lambda (Python)
- Amazon API Gateway (REST)
- Amazon SQS (queue)
- Amazon SES (email)
- Amazon S3 + CloudFront (static hosting)
- HTML, CSS, JavaScript

## 🧠 Features
- Validates credit card input before submission
- Generates random product IDs
- Queues messages for async email confirmation
- Sends emails securely via SES
- Fully serverless — zero EC2s!

## 🚀 Setup Instructions
1. Deploy both Lambda functions.
2. Create an SQS queue (`shippingQueue`).
3. Create an SES verified email (your sender).
4. Set up an API Gateway with Lambda Proxy integration.
5. Enable CORS on API Gateway.
6. Upload `index.html` to S3 and optionally front with CloudFront.

## 📸 Demo
Include screenshots of:
- The HTML form
- CloudWatch logs
- Email confirmation

---

*Built by Hamza Khan as a hands-on AWS learning project.*
