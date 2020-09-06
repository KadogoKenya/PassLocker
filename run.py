#!/usr/bin/env python3.6
import string
import random

from user import userAccount

def create_userDetails(first_name,last_name,phone_number,email,user_name, password):
    new_userDetails= userAccount(first_name,last_name,phone_number,email,user_name, password)
    return new_userDetails

def save_userDetails(userDetails):
    userDetails.save_user()

def main():
    print("Hello Welcome to your account password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user account, dc - display user accounts,ex -exit ")

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

                            # while True:
                            #     print("Use these short codes : gg - create a generate password, ex -exit the lock entry")

                                

                            print("create password: Do you want password generated or you type? use gg - to generate, ex -exit the lock entry")
                            short_code = input().lower()
                            if short_code == 'gg':

                                # print(string.printable)

                                def generatePassword(num):
                                    password=''

                                    for n in range(num):
                                        x = random.randint(0,94)
                                        password += string.printable[x]
                                    return password


                                password_length = int(input("Enter the length of password"))

                                print (generatePassword(password_length))
                                break
                                # print ('\n')

                            elif short_code == "ex":
                                print("Bye .......")
                                break
                            else:
                                print("enter password")

                                password = input()
                                break
                                print ('\n')
                                

                            save_userDetails(create_userDetails(first_name,last_name,phone_number,email,user_name, password)) 
                            print ('\n')
                            print(f"new_userDetails {first_name} {last_name} created")
                            print ('\n')


if __name__ == '__main__':
    main()
