import boto3
from pprint import pprint
import sys

ec2_console = boto3.session.Session(profile_name='botoUser') #Enter your user profile name in 'botoUser', you need to configure credentials for that user 

volume_client = ec2_console.client(service_name='ec2', region_name='us-east-1')

volume_resource = ec2_console.resource(service_name='ec2', region_name='us-east-1')

#================== List all volumes in your account =========================================================

response = volume_client.describe_volumes()['Volumes']
# pprint(response)
for each_item in response:
    print("The volume id is: {}\nThe AvailabilityZone is: {}\nThe volume state is: {}".format(each_item['VolumeId'], each_item['AvailabilityZone'], each_item['State']))
    print("=========================================")


#================== Delete Not used Volume IDs ===============================================================

while True:
    print ("This script perfoms the following actions on ec2 intance")
    print("""
    1. delete not used Volumes
    2. exit
    """)
    
    opt=int(input("Enter your choice: "))
    
    if opt==1:
        volume_id=input("Enter volume id that you want to delete: ")
        volumeID = volume_resource.Volume(volume_id)
        print(dir(ec2_object))
        print ("Terminating EBS Volumes.......")
        volumeID.terminate()
    
    elif opt==2:
        print("Exiting, thank you for usig this script")
        sys.exit()

    else:
        print("Your option is invalid please enter correct option or press 2 to exit the script")