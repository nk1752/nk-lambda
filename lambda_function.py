import boto3
import json
import os
#from dotenv import load_dotenv
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

from creds import get_access_key_id, get_secret_access_key

#load_dotenv()

def lambda_handler(event, context):

    print("************  Hello from Lambda & Nadeem! ************")

    buckets = []

    logger.info("create s3 client")
    s3_client = boto3.client('s3')

    


    return {
        'statusCode': 200,
        'body': json.dumps(event)

    }