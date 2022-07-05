import boto3

ec2_client =boto3.client(service_name='ec2', region_name='us-east-1')
#################### Describe Regions #########################################
us_regions = {'Name':'region-name', 'Values':['us-east-1', 'us-east-2']}
all_regions=[]
for each_region in ec2_client.describe_regions(Filters=[us_regions])['Regions']:
    all_regions.append(each_region['RegionName'])


for each_region in all_regions:
    print("Working on {}".format(each_region))
    ec2_client=boto3.client(service_name='ec2', region_name=each_region)
    list_of_volume_ids = []
    enesai_volume_ids = {'Name':'tag:Name', 'Values':['boto3']}
    paginator = ec2_client.get_paginator('describe_volumes')
    for each_page in paginator.paginate(Filters=[enesai_volume_ids]):
        for each_vol in each_page['Volumes']:
            list_of_volume_ids.append(each_vol['VolumeId'])
    print("The list of volids are: ", list_of_volume_ids)
    
    if bool(list_of_volume_ids)==False:
        continue
    snapshot_ids = []
    for each_volid in list_of_volume_ids:
        print("Taking snap of {}". format(each_volid))
        response = ec2_client.create_snapshot(
            Description="Taking Snapshots with Lambda",
            VolumeId=each_volid,
            TagSpecifications=[
                {
                    'ResourceType':'snapshot',
                    'Tags':[
                        {
                            'Key':"Name",
                            'Value':'enesai'
                        }
                    ]
                }
            ]

        )
        snapshot_ids.append(response.get('SnapshotId'))
    print("The snpa ids are: ",snapshot_ids)
    waiter = ec2_client.get_waiter('snapshot_completed')
    waiter.wait(SnapshotIds=snapshot_ids)
    print("Successfully completed snaps for the volumes of {}".format(list_of_volume_ids))
