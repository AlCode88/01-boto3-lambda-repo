import boto3
from pprint import pprint #### will give you the print in more human readable format


creat_instance = boto3.client(service_name='ec2', region_name = 'us-east-1')

response = creat_instance.describe_instances()['Reservations']
pprint (response)

############################# EC2 Instance get the informatio ###########################
for each_item in response:
     # print(each_item['Instances'])
     for each in each_item['Instances']:
         print("============================")
         print (f"The Image Id is: {each['ImageId']}\nThe Instance Id is: {each['InstanceId']}\nThe instance Lauch Time is: {each['LaunchTime'].strftime('%Y-%m-%d')}")
         