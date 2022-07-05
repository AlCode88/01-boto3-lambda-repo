import boto3
import time

aws_console = boto3.session.Session(profile_name='botoUser')

ec2 = aws_console.resource(service_name='ec2', region_name='us-east-1')

#ec2_client = aws_console.client(service_name='ec2', region_name='us-east-1')
#===========================================================================


my_instance = ec2.Instance('i-0eb039bae19a82184')
# print(dir(my_instance))
print ("Starying Instance ...... ")
my_instance.start()
my_instance.wait_until_running()  # there is a method under isntance that will wait. You can list is using dir option
print("Now my isntance is up and running") 