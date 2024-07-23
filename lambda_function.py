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

    print("Hello from Lambda & Nadeem!")

    # log test
    logger.info("Testing 1")
    logger.info("Testing 2")
    logger.info(os.environ)


    logger.info("create s3 client")
    s3_client = boto3.client('s3')

    logger.info("get list of buckets")
    bucket_list = s3_client.list_buckets()
    logger.info(bucket_list)

    # print all buckets
    for bucket in bucket_list['Buckets']:
        print(f'- {bucket["Name"]}')

    

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda & Nadeem!')
    }