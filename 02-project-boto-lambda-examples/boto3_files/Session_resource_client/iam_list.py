import boto3
aws_mag_con = boto3.session.Session(profile_name ="talant") # this is a session and you can create as much sesssion as you want per profile.

iam = boto3.client('iam')


for user in iam.list_users()['Users']:
 print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
 user['UserName'],
 user['UserId'],
 user['Arn'],
 user['CreateDate']
 )
 )