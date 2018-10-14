import json

import requests

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# DynamoDB setting
import boto3
from boto3.dynamodb.conditions import Key, Attr
ENDPOINT = 'http://192.168.0.21:8000'
TABLE = 'helloworld'
KEY_NAME = 'username'

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb", endpoint_url=ENDPOINT)
    table = dynamodb.Table(TABLE)
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