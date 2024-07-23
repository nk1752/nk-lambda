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

    # log event and context
    logger.info("Event --> ", event)
    logger.info("Context --> ", context)
    # log environment variables
    logger.info("env vars --> ",os.environ)


    logger.info("create s3 client")
    s3_client = boto3.client('s3')

    logger.info("get list of buckets")
    response = s3_client.list_buckets()
    logger.info(response)

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
        bucket_list += bucket['Name']

    

    return {
        'statusCode': 200,
        # add a header to the response
        'headers': {'Content-Type': 'application/json'},
        # return bucket_list as JSON
        'body': json.dumps(bucket_list)
    }