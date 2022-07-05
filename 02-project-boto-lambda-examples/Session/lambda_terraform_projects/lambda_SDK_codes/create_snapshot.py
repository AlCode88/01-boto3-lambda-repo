import boto3
import json
from datetime import datetime

# Define UTC time zone
now = datetime.now()
time = now.strftime("%m-%d-%Y  %H-%M-%S")


volume = boto3.client(service_name='ec2', region_name='us-east-1')
# pprint(volume.describe_volumes()) to list all volumes 
# you would like to get the volumes
# pprint (volume.describe_volumes()['Volumes'])

#1
# List all volumes 
# for each_volume in volume.describe_volumes()['Volumes']:
#     for each_tags in each_volume['Tags']:
#         for each_value in each_tags['Value']:
#             pprint('env')
#     print('===========================================')

#2
#========= append variable to volumes ====================
# list_of_volumes=[]
# #filter_enesai_volumes={'Name'}

# for each_volume in volume.describe_volumes()['Volumes']:
#     list_of_volumes.append(each_volume['VolumeId'])
# print("The list of avilable volumes are:  ",list_of_volumes)

#3 Filter Names based on Tags
list_of_volumes=[]
enesai_volume_ids = {'Name':'tag:Name', 'Values':['boto3']}

for each_volume in volume.describe_volumes(Filters=[enesai_volume_ids])['Volumes']:
    list_of_volumes.append(each_volume['VolumeId'])
print("The enesai volume ids are:  ",list_of_volumes)


#4 Create a Snapshot with Client
snapshot_ids=[]
for each_snapshot in list_of_volumes:
    current_time = time
    description = "Instance created date"
    print("Taking the snap of {}".format(each_snapshot))
    response=volume.create_snapshot(
        Description="Snapshot created date {current_time}".format(current_time=current_time),
        VolumeId=each_snapshot,
        TagSpecifications=[
        {
            'ResourceType': 'snapshot',
            'Tags': [
                {
                    'Key': 'Created-day',
                    'Value': "{current_time}".format(current_time=current_time),
                },
                {
                    'Key': 'Name',
                    'Value': 'enesai'
                }
            ]
        }
    ]
    )
    snapshot_ids.append(response['SnapshotId'])
print ("The snap ids are: ",snapshot_ids)
waiter = volume.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=snapshot_ids)

print ("Successfully completed snaps for the volumes of: {}".format(list_of_volumes))