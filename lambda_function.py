import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('serverless-web-app')
def lambda_handler(event, context):
    response = table.get_item(Key={
        'id':'0'
    })
    Views = response['Item']['Views']
    Views = Views + 1
    
    print(Views)
    
    response = table.put_item(Item={
        'id':'0',
        'views': Views
    })
    
    return Views
