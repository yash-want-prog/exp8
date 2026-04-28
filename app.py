def lambda_handler(event, context):
    password = "12345"  # Vulnerability for testing
    return {
        'statusCode': 200,
        'body': 'Hello Secure CI/CD'
    }
