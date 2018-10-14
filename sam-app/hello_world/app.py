import json

import requests

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# DynamoDB setting
import boto3
from boto3.dynamodb.conditions import Key, Attr
ENDPOINT = 'http://10.0.2.15:8000'
TABLE = 'helloworld'
KEY_NAME = 'username'

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb", endpoint_url=ENDPOINT)
    table = dynamodb.Table(TABLE)

    # 取得
    if event['httpMethod'] == 'GET':
        key = {KEY_NAME: event['queryStringParameters']['username']}
        logger.info(key)

        # DynamoDBから取得
        ret = table.get_item(Key=key)
        if "Item" not in ret:
            return False
        return {
            "statusCode": 200,
            "body": json.dumps(ret["Item"]),
        }

    # 新規登録
    elif event['httpMethod'] == 'POST':
        item = json.loads(event['body'])
        table.put_item(Item=item)
        return {
            "statusCode": 200,
            "body": json.dumps(item),
        }