import boto3
import time

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = aws_console.resource(service_name='ec2', region_name='us-east-1')

ec2_client = aws_console.client(service_name='ec2', region_name='us-east-1')

#============================================================================

my_instance = ec2_resource.Instance('i-0eb039bae19a82184')
print("Stopping the given instance.........")
my_instance.stop()
waiter = ec2_client.get_waiter('instance_stopped')
waiter.wait(InstanceIds=['i-0eb039bae19a82184'])
print("Now your instance is in stopped condition")