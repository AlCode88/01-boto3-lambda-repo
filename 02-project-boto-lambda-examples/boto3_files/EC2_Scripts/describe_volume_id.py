import boto3
from pprint import pprint

describe_volume = boto3.client(service_name='ec2', region_name = 'us-east-1')

############################## Describe the volume ########################################
response = describe_volume.describe_volumes()['Volumes']
for each_item in response:
    print ("============================")
    print ("The volume id is: {}\nThe AvailabilityZone: {}\nThe VolumeType: {}".format(each_item['VolumeId'], each_item['AvailabilityZone'], each_item['VolumeType']))
