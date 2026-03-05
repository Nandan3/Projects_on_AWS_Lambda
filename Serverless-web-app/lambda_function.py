import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('serverless-web-app')

def lambda_handler(event, context):

    response = table.get_item(
        Key={
            'id': '0'
        }
    )

    # If item doesn't exist, start from 0
    if 'Item' in response:
        views = response['Item']['views']
    else:
        views = 0

    views = views + 1

    print(views)

    table.put_item(
        Item={
            'id': '0',
            'views': views
        }
    )

    return views
