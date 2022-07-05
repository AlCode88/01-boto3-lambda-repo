import boto3
from random import choice

def get_iam_client_object():
    iam_client = boto3.client('iam')
    return iam_client



def get_random_password():
    len_of_password = 30
    valid_characters_password = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMOPQRSTUVWXYZ!@#$%^&*()_+=?><}{[]"
    return "".join(choice(valid_characters_password) for each_letter in range(len_of_password)) 



def main():
    iam_client = get_iam_client_object()
    iam_user_name = "testUserBoto"
    password = get_random_password()
    policyArn = "arn:aws:iam::aws:policy/AdministratorAccess"
    iam_client.create_user(UserName=iam_user_name)
    iam_client.create_login_profile(UserName=iam_user_name, Password=password, PasswordResetRequired=False)
    iam_client.attach_user_policy(UserName=iam_user_name, PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess")
    print("Iam User name ={} and Password={}".format(iam_user_name, password))
    return None


if __name__=="__main__":
   main()