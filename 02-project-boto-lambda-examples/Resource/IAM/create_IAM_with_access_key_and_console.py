import boto3
from random import choice
import sys

def get_iam_client():
    iam_client = boto3.client('iam')
    return iam_client


def get_random_password():
    len_of_password = 15
    valid_characters_password = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMOPQRSTUVWXYZ!@#$%^&*()_+=?><}{[]"
    return "".join(choice(valid_characters_password) for each_password in range(len_of_password))

def main():
    iam_client = get_iam_client()
    iam_user_name = 'botoUser3'
    password = get_random_password()
    policyArn = "arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_client.create_user(UserName=iam_user_name)
    except Exception as e:
        if e.response['Error']['Code'] == "EntityAlreadyExist":
            print ("User with the same name {}".format(iam_user_name))
            sys.exit(0)
        else:
            print("Please verify the followin error and retry")
            print(e)
            sys.exit(1)
    create_credentials = iam_client.create_access_key(UserName=iam_user_name)
    print("IAM User Name={}".format(iam_user_name))
    print("AccessKeyId={}\nSecretAccessKey={}".format(create_credentials['AccessKey']['AccessKeyId'],create_credentials['AccessKey']['SecretAccessKey']))
    iam_client.create_login_profile(UserName=iam_user_name,Password=password,PasswordResetRequired=False)
    iam_client.attach_user_policy(UserName=iam_user_name,PolicyArn=policyArn)
    print ("IAM User Name={} and Password={}".format(iam_user_name,password))
    return None

if __name__=="__main__":
    main()