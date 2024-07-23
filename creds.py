# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError

import os


def get_access_key_id():
        secret_name = "lambda/access-key-id"
        region_name = "us-east-1"

        # Create a Secrets Manager client
        session = boto3.session.Session(
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
            region_name=region_name
        )
        client = session.client(
            service_name='secretsmanager'
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            # For a list of exceptions thrown, see
            # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            raise e
        
        secret = get_secret_value_response['SecretString']
        return secret
    
def get_secret_access_key():
        secret_name = "lambda/secret-access-key"
        region_name = "us-east-1"

        # Create a Secrets Manager client
        session = boto3.session.Session(
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
            region_name=region_name
        )
        client = session.client(
            service_name='secretsmanager'
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            # For a list of exceptions thrown, see
            # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            raise e
        
        secret = get_secret_value_response['SecretString']
        return secret
