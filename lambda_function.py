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
    logger.info(context)

    logger.info("*** Testing get_access_key_id ***")
    id = get_access_key_id()
    logger.info("*** Testing get_secret_access_key ***")
    key = get_secret_access_key()

    logger.info("id: ", id)
    logger.info("key: ", key)
    
    aws_access_key_id=id
    aws_secret_access_key=key
    region_name='us-east-1'

    logger.info("aws_access_key_id --> ",aws_access_key_id)
    logger.info("aws_secret_access_key --> ", aws_secret_access_key)

    # Create an S3 client
    session = boto3.Session(aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key,
                            region_name=region_name)
    s3 = session.client('s3')
    
    
    print("Call S3 to list current buckets")
    response = s3.list_buckets()
    
    print("response: ", response)
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    # Print out the bucket list
    print("Bucket List: %s" % buckets)
    # print bucket owner
    print("bucket owner: ", response['Owner'])
    # print bucket count
    print("bucket count: ", len(buckets))
    # print bucket names
    print("bucket names: ", buckets)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda & Nadeem!')
    }