import json, boto3

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    sns = boto3.client('sns')
    number = '+447123456789'
    sns_response = sns.publish(PhoneNumber = number, Message='example text message' )

    response = {
        "statusCode": 200
    }

    return response