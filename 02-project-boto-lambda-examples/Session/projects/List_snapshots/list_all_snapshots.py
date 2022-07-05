import boto3

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = aws_console.resource(service_name='ec2', region_name='us-east-1')

ec2_client = aws_console.client(service_name='ec2', region_name='us-east-1')

sts = aws_console.client(service_name='sts', region_name='us-east-1')

#======================== Get the account ID ===================================
response = sts.get_caller_identity()
# print(response)                               - will list a dictionary
# print(dir(response))                          - will list all available methods that you can perform
print(response.get('Account'))

#======================= List all available snpashots ===========================
#for each_snap in ec2_resource.snapshots.all():
#    print(each_snap)

#======================= List all available snpashots owned by you ===============
my_account_id = response.get('Account')
for each_snap in ec2_resource.snapshots.filter(OwnerIds=[my_account_id]):
    print(each_snap)

#======================== List all snaps using Client ===============================
my_account_id = response.get('Account')

response = ec2_client.describe_snapshots(OwnerIds=[my_account_id])
print(response)
#for each_snap_client in ec2_client.describe_snapshots.filters(Filters=OwnerIds[my_account_id]):
#    print(each_snap_client)
for each_snapshots in ec2_client.describe_snapshots(OwnerIds=[my_account_id]):
    print(each_snapshots)