import boto3
import datetime

client = boto3.client(service_name='ec2', region_name='us-east-1')

snaps = {'Name':'tag:Name', 'Values':['enesai']}
SnapshotIds =[]

# List all Enesai Snapshots
enesai_snapshots = client.describe_snapshots(Filters=[snaps])['Snapshots']
#print(enesai_snapshots)

for each_snap_id in client.describe_snapshots(Filters=[snaps])['Snapshots']:
    SnapshotIds.append(each_snap_id['SnapshotId'])
print(SnapshotIds)

#Delete Enesai Snapshots
for each_enesai_snap in SnapshotIds:
    print("Deleting Enesai snaps of {}".format(each_enesai_snap))
    response = client.delete_snapshot(
    SnapshotId=each_enesai_snap
)
print("Enesai Snapshots has been deleted")