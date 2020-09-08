#!/usr/bin/env python3.6
import string
import random

from user import userAccount
from user import userCredentials
# import pyperclip

'''
userAccount class-method definations
'''

def create_user(first_name,last_name,phone_number,email,user_name,):
    
    userDetails= userAccount(first_name,last_name,phone_number,email,user_name)
    
    return userDetails

def save_users(user):
    user.save_user()

def del_details(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_details(number):
    '''
    Function that finds a contact by number and returns the user
    '''
    return userAccount.find_detail_by_number(number)

def check_existing_details(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return userAccount.details_exists(number)


def display_user():
    '''
    Function that returns all the saved contacts
    '''
    return userAccount.display_user()


def create_credential(username,email,phone_number,password):
    
    credentials= userCredentials(username,email,phone_number,password)
    
    return credentials

def save_credentials(user):
    user.save_credentials()

def del_credentials(user):
    '''
    Function to delete a user
    '''
    user.delete_credentials()

def display_credential():
    '''
    Function that returns all the saved contacts
    '''
    return userCredentials.display_credential()

'''
userCredentials class defination
'''

def main():
    print("Hello Welcome to your account password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user details, dc - display user details,fu-find user,lg-login, dcr-display credentials ex -exit ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New User details")
            print("-"*10)

            print ("First name ....")
            first_name = input()

            print("Last name ...")
            last_name = input()

            print("Email address ...")
            email = input()

            print("Phone number ...")
            phone_number = input()

            print("User Name ...")
            user_name = input()


            save_users(create_user(first_name,last_name,phone_number,email,user_name)) 
            
            print ('\n')
            print(f"new_userDetails {first_name} {last_name} created")
            print ('\n')
            # break

        elif short_code == 'dc':

            if display_user():
                    print("Here is a list of all your contacts")
                    print('\n')

                    for detail in display_user():
                        print(f"{detail.first_name} {detail.last_name} {detail.user_name} {detail.email}...{detail.phone_number}")
                    print('\n')
            else:
                    print('\n')
                    print("You dont seem to have any contacts saved yet")
                    print('\n')
                    # break

        elif short_code == 'fu':

            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_details(search_number):
                    search_user = find_details(search_number)
                    print(f"{search_user.first_name} {search_user.last_name}")
                    print('-' * 20)

                    print(f"Phone number.......{search_user.phone_number}")
                    print(f"Email address.......{search_user.email}")
            else:
                    print("That contact does not exist")

        elif short_code=='lg':

            print("New User credential")
            print("-"*10)

            print("username...")
            username = input()

            print ("Email ....")
            email= input()

            print("Number...")
            phone_number = input()

            # print("Password...")
            # username = input()

            # print("use short-codes gn-the system to generate a password for you, cp-to create your own password...")
            # email = input()
            
            while True:
                print("use short-codes gp-the system to generate a password for you, cp-to create your own password...")

                short_code = input().lower()

                if short_code == 'gp':

                    def generatePassword(num):
                        password=''

                        for n in range(num):
                            x = random.randint(0,94)
                            password += string.printable[x]
                        return password


                    password_length = int(input("Enter the length of password"))

                    print (generatePassword(password_length))
                    break

                elif short_code == 'cp':
                    print("Enter your password here")
                    password=input()
                    break

                else:
                    print("No password created")
                    break
        
            save_credentials(create_credential(username,email,phone_number,password)) 
            
            print ('\n')
            print(f"new_credentials {username} {email} created")
            print ('\n')

        elif short_code == 'dcr':

            if display_credential():
                print("Here is a list of all your contacts")
                print('\n')
                

                for credential in display_credential():
                    print(f"{credential.username} {credential.email} {credential.number} {credential.password}")
                print('\n')
        else:
                print('\n')
                print("You dont seem to have any contacts saved yet")
                print('\n')


if __name__ == '__main__':
    main()
