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

'''
userCredentials class defination
'''

def main():
    print("Hello Welcome to your account password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user details, dc - display user details,fu-find user, ex -exit ")

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
            if check_existing_contacts(search_number):
                    search_contact = find_contact(search_number)
                    print(f"{search_contact.first_name} {search_contact.last_name}")
                    print('-' * 20)

                    print(f"Phone number.......{search_contact.phone_number}")
                    print(f"Email address.......{search_contact.email}")
            else:
                    print("That contact does not exist")

        

if __name__ == '__main__':
    main()
