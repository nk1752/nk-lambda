import boto3
import json
import os
#from dotenv import load_dotenv

from creds import get_access_key_id, get_secret_access_key

#load_dotenv()

def lambda_handler(event, context):

    print("Hello from Lambda & Nadeem!")

    # print context
    print("aws_request_id: ", context.aws_request_id)
    print("function_name: ", context.function_name)
    print("function_version: ", context.function_version)
    print("invoked_function_arn: ", context.invoked_function_arn)
    print("memory_limit_in_mb: ", context.memory_limit_in_mb)
    print("log_group_name: ", context.log_group_name)
    print("** Testing 2 **")
    
    aws_access_key_id=get_access_key_id()
    aws_secret_access_key=get_secret_access_key()
    region_name='us-east-1'

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