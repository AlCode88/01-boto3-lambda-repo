#!/bin/bash
#
# 
#
###################### Script Introduction #############################
echo "##################################################################"
echo
echo "This script Uploads your folder to S3 bucket"
sleep 3
echo "Please select bucket name and provide full path to your Directory"
sleep 3
echo "Example: Select the bucket name from the list: test-bucket"
echo "          Give Full path to the Directory: /home/ec2-user/Boto3_Lambda_Codes/Session"
sleep 6
echo "Run 'pwd' - to get the full path to your home directory"

echo "###################################################################"
echo "Listing all available buckets...."
sleep 3
aws s3 ls

echo "###################################################################"
echo -n "Please select the bucket name that you want to upload your Directory: "
read bucketName
sleep 3

echo "###################################################################"
echo -n "Please enter a full path for the Dir: "
read filePath

if aws s3 sync $filePath s3://$bucketName
then
    echo "Your Directory is successfully uploaded to the bucket"
    echo
    echo "Listing uploaded file in your s3 bucket"
    echo
    sleep 3
    aws s3 ls s3://$bucketName
else
    echo "The bucket name or the file path is incorrect or file already exists in the bucket please check"
    aws s3 ls s3://$bucketName
fi
echo "###################################################################"
