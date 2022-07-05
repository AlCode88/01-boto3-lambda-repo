import boto3

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = aws_console.resource(service_name='ec2', region_name='us-east-1')

sts_client = aws_console.client(service_name='sts', region_name='us-east-1')
#=================== Get Account id ============================================
response = sts_client.get_caller_identity()

my_own_id = response.get('Account')

#=================== List all snaps ============================================
snap_size = {"Name":"volume-size", "Values":['16']} # -stands in GB
#prod_tag = {"Name":"tag:env", "Values":['prod']}
#dev_tag = {"Name":"tag:env", "Values":['dev']}
for each_snap in ec2_resource.snapshots.filter(OwnerIds=[my_own_id],Filters=[snap_size]): # you can define the snap size in variables
    print(each_snap)