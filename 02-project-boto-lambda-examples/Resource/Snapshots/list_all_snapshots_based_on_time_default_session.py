import boto3
import datetime

ec2_resource = boto3 .resource(service_name='ec2', region_name='us-east-1')

sts_client = boto3.client(service_name='sts', region_name='us-east-1')

ec2_client = boto3.client(service_name='ec2', region_name='us-east-1')
#=================== Get Account id ============================================
response = sts_client.get_caller_identity()

my_own_id = response.get('Account')

#=================== List all snaps based on creation time =====================
today = datetime.datetime.now()
start_time = datetime.datetime(today.year, today.month, today.day, 4,15,44) # to list all snaps at the same time
print (start_time)
for each_snap in ec2_resource.snapshots.filter(OwnerIds=[my_own_id]):
    #print(dir(each_snap))  - to list all available operations
    #print (each_snap.start_time)
    print (each_snap.id,each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S"))