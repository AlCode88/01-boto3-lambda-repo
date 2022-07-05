import boto3
from pprint import pprint

list_enesai_instances=[]
enesai_instances_ids = {'Name':'tag:env', 'Values':['prod']}

instances = boto3.client(service_name='ec2', region_name='us-east-1')

for each_instance in instances.describe_instances(Filters=[enesai_instances_ids])['Reservations']:
    for each_instanceId in each_instance['Instances']:
        list_enesai_instances.append(each_instanceId['InstanceId'])
print("List of enesai Instances: {}".format(list_enesai_instances))

# Create Images From the List of instances
image_ids=[]
for each_images in list_enesai_instances:
    print("Taking a Snapshot of {}".format(each_images))
    response = instances.create_image(
    InstanceId=each_images,
    Name=unique_name
    # TagSpecifications=[
    #         {
    #             'ResourceType': 'instances',
    #             'Tags': [
    #                 {
    #                     'Key': 'Delete-on',
    #                     'Value': '90'
    #                 },
    #                 {
    #                     'Key': 'Name',
    #                     'Value': 'enesai'
    #                 }
    #             ]
    #         }
    #     ]
    )
#    image_ids.append(response['ImageId'])
#print("The new prod images: ", image_ids)