# pre-requesites to have python3.~
# we will use modules choice and module random
# we will use .append method and .join methods 

#==================== Step1 import module choice from module random =========================================
from random import choice


#============= Step2 Define your custom variables =============================================================
len_of_password = 10
valid_characters_password = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMOPQRSTUVWXYZ!@#$%^&*()_+=?><}{[]"
password = []
#print(choice(valid_characters_password))

'''
#============ 1st Logic to create a random password ===========
for each_password in range(len_of_password):
    #print(choice(valid_characters_password))
    password.append(choice(valid_characters_password))
#print("".join(password))

random_password = "".join(password)
print(random_password)
'''


#=============== 2nd Logic to create a random password================================================
random_password = "".join(choice(valid_characters_password) for each_letter in range(len_of_password)) 
print(random_password)