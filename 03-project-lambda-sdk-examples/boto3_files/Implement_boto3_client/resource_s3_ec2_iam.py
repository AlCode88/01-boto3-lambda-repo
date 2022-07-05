import boto3

aws_man_con = boto3.session.Session(profile_name='botoUserTest')

iam_resource = aws_man_con.resource(service_name='iam', region_name='us-east-1')
ec2_resource = aws_man_con.resource(service_name='ec2', region_name='us-east-1')
s3_resource = aws_man_con.resource(service_name='s3', region_name='us-east-1')

# List IAM users with resource

#print(iam_resource.users.all())

for iam_user in iam_resource.users.all():
# for iam_user in iam_resource.users.limit(1):
    # print(dir(iam_user))
    print(iam_user.user_name)

# S3 print buckets
for each_s3 in s3_resource.buckets.all():
    print(each_s3.name)


# EC2 print ec2 id
for each_ec2 in ec2_resource.instances.all():
    print(each_ec2.id)