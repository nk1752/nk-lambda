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
    print("event keys: ", event.get("key1"))
    print("context keys: ", context.get("value1"))

    print("invoked_function_arn: ", context.invoked_function_arn)
    print("memory_limit_in_mb: ", context.memory_limit_in_mb)
    print("log_group_name: ", context.log_group_name)
    print("log_stream_name: ", context.log_stream_name)
    print("function_name: ", context.function_name)
    print("function_version: ", context.function_version)
    print("aws_request_id: ", context.aws_request_id)


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