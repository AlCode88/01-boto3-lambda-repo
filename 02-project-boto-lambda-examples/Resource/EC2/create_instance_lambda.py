import boto3
import os
import json

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    instance = ec2.create_instances(
      ImageId=AMI,
      InstanceType=INSTANCE_TYPE,
      KeyName=KEY_NAME,
      MinCount=1,
      MaxCount=1 
    )
    
    print("New Instance Created", instance[0].id)