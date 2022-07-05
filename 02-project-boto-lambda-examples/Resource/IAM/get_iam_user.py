import boto3

#===================== list all available users ============================
client = boto3.client('iam') 
response = client.list_users()
 
for x in response['Users']:
    print (x['UserName']) 
print("======================")


#===================== list all available users ============================
users = client.list_users()
for key in users['Users']:
    print (key['UserName'])
print("======================")

#===================== list all available policies =========================
for key in users['Users']:
    List_of_Policies =  client.list_user_policies(UserName=key['UserName'])
    for key in List_of_Policies['PolicyNames']:
        print (key['PolicyName'])
print("========================")

#===================== list all users with enabled MFA ======================
for key in users['Users']:
    List_of_MFA_Devices = client.list_mfa_devices(UserName=key['UserName'])
    for key in List_of_MFA_Devices['MFADevices']:
        print (key)