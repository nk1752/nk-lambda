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

    
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"]
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
    region_name='us-east-1'

    logger.info("Creating session")
    session = boto3.Session(aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key,
                            region_name=region_name)
    
    logger.info("Creating S3 client")
    s3 = session.client('s3')
    
    
    logger.info("Listing buckets")
    response = s3.list_buckets()
    
    logger.info(response)

    logger.info("Printing bucket list")
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