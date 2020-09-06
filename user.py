import string
import random

class userAccount:
    """
    Class that generates new instances of a userAccounts
    """


    # contact_list = []

    user_details=[]

    def __init__(self,first_name,last_name,phone_number,email,user_name,):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New first name.
            first_name: New last name.
            number: New phone number.
            email : New  email address.
            user_name : New  user name.

        '''
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.user_name=user_name
        # self.password=password

    def save_user(self):
        userAccount.user_details.append(self)



class userCredentials:
    """
    Class that generates new instances of a userCredentials
    """

    user_credentials=[]

    def __init__(self,username,number,password):

            '''
            __init__ method that helps us define properties for our objects.

            self.username = username
            self.password = password
            self.number=number
            '''

    def save_credential(self):
        userCredentials.user_credentials.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved contact from the contact_list
        '''
        userCredentials.user_credentials.remove(self)


    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a usename and returns a contact that matches that number.

        Args:
            username: username to search for
        Returns :
            credentials.
        '''

        for credential in cls.user_credentials:
            if credential.number == number:
                return credential

                
        #          def find_by_number(cls,number):
        # '''
        # Method that takes in a number and returns a contact that matches that number.

        # Args:
        #     number: Phone number to search for
        # Returns :
        #     Contact of person that matches the number.
        # '''

        # for contact in cls.contact_list:
        #     if contact.phone_number == number:
        #         return contact