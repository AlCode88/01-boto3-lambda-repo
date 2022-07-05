import boto3
from pprint import pprint

ec2_console = boto3.session.Session(profile_name='botoUser')

ec2 = ec2_console.client(service_name='ec2', region_name='us-east-2')

response = ec2.describe_instances()['Reservations']

#1 We will print the output first
#pprint(response) #will give you key:value option 
#------------------------------------------------

#2 Print instances
# for each_item in response:
#         print(each_item['Instances'])

#3 To iterrate 2 times and get the instance id
# for each_item in response:
#     for each_instanceID in each_item['Instances']:
#         print(each_instanceID['ImageId'])

for each_item in response:
   for each_info in each_item['Instances']:
       print("The image id is: {}\nThe instance id is: {}\nThe Instance Launch Time is: {}".format(each_info['ImageId'], each_info['InstanceId'], each_info['LaunchTime'].strftime("%Y-%m-%d")))
       print("=======================================")