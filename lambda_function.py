import boto3
import json
import os
#from dotenv import load_dotenv
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

from src.creds import get_access_key_id, get_secret_access_key


#load_dotenv()

def lambda_handler(event, context):

    print("************  Hello from Lambda & Nadeem! ************")


    # parse the event object and get the name of the bucket
    logger.info(event)

    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:",  context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    # We have added a 1 second delay so you can see the time remaining in get_remaining_time_in_millis.
    #time.sleep(1) 
    print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())

    buckets = []

    logger.info("create s3 client")
    s3_client = boto3.client('s3')

    logger.info("get list of buckets")
    response = s3_client.list_buckets()
    logger.info(response)

    # Output the bucket names in list
    print('Existing buckets:')
    bucket_count = 0
    for bucket in response['Buckets']:
        #print(f'  {bucket["Name"]}')
        buckets.append(bucket["Name"])
        bucket_count += 1

    logger.info(buckets)

    message = f"Hello {event['first_name']} {event['last_name']}! you have {bucket_count} buckets in your account."


    return {
        # return buckets JSON object
        "message": message,
        "buckets": json.dumps(buckets)

    }