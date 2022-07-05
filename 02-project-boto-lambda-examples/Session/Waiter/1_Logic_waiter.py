import boto3
import time

aws_console=boto3.session.Session(profile_name='botoUser')

ec2 = aws_console.resource(service_name='ec2', region_name='us-east-1')

ec2_client = aws_console.client(service_name='ec2', region_name = 'us-east-1')
#=============================================================================

my_instance = ec2.Instance("i-0eb039bae19a82184")

print ("Starting Instance..............")

# to get the current status of your isntance state 
print(my_instance.state)

# print (dir(my_instance))
my_instance.start()

while True:
    my_instance_object=ec2.Instance("i-0eb039bae19a82184")
    print("The current status of ec2 is:  ",my_instance_object.state['Name'])
    if my_instance_object.state['Name']=="running":
        break
    print("Waiting to get running status .......")
    time.sleep(5)

print("Isntance is up and running now")