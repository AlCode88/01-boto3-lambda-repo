import boto3
import time

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = aws_console.resource(service_name='ec2', region_name='us-east-1')

ec2_client = aws_console.client(service_name='ec2', region_name='us-east-1')

#===============================================================================

my_instance = ec2.Instance("i-0eb039bae19a82184")

print("Stoping the isntance.......")

my_instance.stop()
my_instance.wait_until_stopped()
print("Now your instance is in stopped condition")