import boto3
import datetime
#=============== List all iams with client =============
iam_users = boto3.client('iam')
#
#
response = iam_users.list_users()
#print(response)

for x in response['Users']:
    print(x['UserName'])

#================ List all iam with resource ===========
iam_response = boto3.resource('iam')
print(iam_response)
#
for iam_user in iam_response.users.all():
    
# for iam_user in iam_resource.users.limit(1):
    # print(dir(iam_user))
    print("=================================")
    # print(iam_user.user_name, iam_user.user_id, iam_user.arn)
    print ("The user name is: {}\nThe user name: {}\nThe userArn: {}".format(iam_user.user_name, iam_user.user_id, iam_user.arn))

# for the list use >>> print ("The volume id is: {}\nThe AvailabilityZone: {}\nThe VolumeType: {}".format(each_item['VolumeId'], each_item['AvailabilityZone'], each_item['VolumeType']))