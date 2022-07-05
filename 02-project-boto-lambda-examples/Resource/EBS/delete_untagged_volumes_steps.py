import boto3

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_client = aws_console.client(service_name='ec2', region_name='us-east-1')

# Step1 make a all available list

# print(ec2_client.describe_volumes()['Volumes'])                      - go to the documentation in the client section look for describe intance it should pring you a list

# Step2 make a all available list
# for each_volume in ec2_client.describe_volumes()['Volumes']:         - to narrow down the list in the available options 
#     print(each_volume)
#     print("================================")

# Step3
for each_volume in ec2_client.describe_volumes()['Volumes']: 
    #print(each_volume)
    #break
    if not 'Tags' in each_volume and each_volume['State']=='available':
        #print(each_volume['VolumeId'])
        print('Deleting ', each_volume['VolumeId'])
        print("================================")
        ec2_client.delete_volume(VolumeId=each_volume['VolumeId'])

print ("Deleted all untagged and available volumes")