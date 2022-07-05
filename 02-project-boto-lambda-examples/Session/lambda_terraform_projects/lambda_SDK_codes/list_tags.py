import boto3

ec2_tags= boto3.client(service_name='ec2', region_name='us-east-1')

sts = boto3.client(service_name='sts', region_name='us-east-1')

response = sts.get_caller_identity()
account_id = response.get('Account')

#my_snaps = ec2_tags.describe_snapshots(OwnerIds=[account_id])



for each_item in ec2_tags.describe_volumes()['Volumes']:
	if not "Tags" in each_item  and each_item['State']=='available':
		print('Deleting ',each_item['VolumeId'])
		ec2_con_cli.delete_volume(VolumeId=each_item['VolumeId'])
print("Delete all unused and untagged volumes.")