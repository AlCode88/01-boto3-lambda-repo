import boto3
import time

aws_console = boto3.session.Session(profile_name='botoUser')

ec2 = aws_console.resource(service_name='ec2', region_name='us-east-1')

ec2_client = aws_console.client(service_name='ec2', region_name='us-east-1')

#===========================================================================
# Client will check the isntance up to 15 seconds

print("starting ec2 isntance.....")
# print(dir(ec2_client))

print("Preparing Instance to start")
ec2_client.start_instances(InstanceIds=["i-0eb039bae19a82184"])
waiter = ec2_client.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-0eb039bae19a82184'])
print("Now your ec2 instance is up and running")