import boto3
from datetime import datetime

########### Variables and Clients ######################
ec2_re=boto3.resource(service_name="ec2",region_name="us-east-1")                                                       
vol_ids=[]
enesai_volume_ids = {'Name':'tag:Name', 'Values':['enesai']}                                                                                                                
enesai_snaps = {'Name':'tag:Name', 'Values':['enesai']}
snapshot_ids=[]

snap_ids=[]
########### Colleting volume Ids ###################################           
for each_vol in ec2_re.volumes.filter(Filters=[enesai_volume_ids]):                                                                                                                                                                         
    vol_ids.append(each_vol.id)                                                                                                                                                                                                              
print('All volume ids are: ',vol_ids)              
                                                                                                                          
########## Creating snapshots for tagged volumes ###################### 
                                                                                                               
for each_vo_id in vol_ids:                                                                                                
    response= ec2_re.create_snapshot(                                                                                      
    Description='Snap with Lambda',                                                                                       
    VolumeId=each_vo_id,                                                                                                  
    TagSpecifications=[                                                                                                   
        {                                                                                                              
            'ResourceType': 'snapshot',                                                                                   
             'Tags': [                                                                                                    
                {                                                                                                         
                    'Key': 'Delete-on',                                                                                   
                    'Value':'90'                                                                                          
                },
                {                                                                                                         
                    'Key': 'Name',                                                                                   
                    'Value':'enesai'                                                                                          
                },
                {                                                                                                         
                    'Key': 'env',                                                                                   
                    'Value':'prod'                                                                                          
                }                                                                                                        
            ]                                                                                                   
        }                                                                                                               
    ]                                                                                                                  
)                                                                                                                    
snap_ids.append(response.id)                                                                                           
                                                                                             
###########Creating waiter using client ######################## 
ec2_cli=boto3.client(service_name="ec2",region_name="us-east-1")                                                        
waiter = ec2_cli.get_waiter('snapshot_completed')                                                                         
waiter.wait(SnapshotIds=snap_ids)

########## Define UTC time zone ##########
now = datetime.now()
time = now.strftime("%m-%d-%Y  %H-%M-%S")

############## Variables and boto client ###########################################################
list_ec2_snaps = boto3.client(service_name='ec2', region_name='us-east-1')

################## List all snapshots   ######################################################################
for each_snap in list_ec2_snaps.describe_snapshots(Filters=[enesai_snaps],OwnerIds=['self'])['Snapshots']:
    snapshot_ids.append(each_snap['SnapshotId'])
print(snapshot_ids)

################# create a AMI from snapshops ######################
def creat_images_from_snap():
    response = list_ec2_snaps.describe_instances(Filters=[enesai_snaps])
    instance_id = []
    for reservation in response['Reservations']:
        for instances in reservation['Instances']:
            instance_id.append(instances['InstanceId'])
    print(instance_id)

    for snapshots in snapshot_ids:
        print("Creating Imagesf for snaps {}".format(snapshots))
        ids = instance_id
        name="enesai-{time}-{instances}".format(time=time,instances=ids)   #name = "App_AMI_{instance_id}_{current_time}".format(instance_id=instance_id,current_time=current_time)
        image = list_ec2_snaps.register_image(
            BlockDeviceMappings=[
                 {
                    'DeviceName': '/dev/sda1',
                    'Ebs': {
                        'DeleteOnTermination': True,
                        'SnapshotId':snapshots,
                        'VolumeSize': 8,
                        'VolumeType': 'gp2'
                    }
                 },
            ],
            Description='create enesa AMIs',
            Name=name,
            RootDeviceName='/dev/sda1',
            VirtualizationType='hvm'
        )
    waiter = ec2_client.get_waiter('image_available')
    waiter.wait(ImageIds=image_ids)
    print("Images has been created")
creat_images_from_snap()