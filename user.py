import string
import random
import pyperclip

class userAccount:
    """
    Class that generates new instances of a userAccounts
    """


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

    @classmethod
    def details_exists(cls,phone_number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the details exists
        '''
        for detail in cls.user_details:
            if detail.phone_number == phone_number:
                return True
        return False

    @classmethod
    def find_detail_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            userdetails of person that matches the number.
        '''

        for detail in cls.user_details:
            if detail.phone_number == number:
                return detail

    @classmethod
    def copy_email(cls,number):
        detail_found = userAccount.find_detail_by_number(number)
        pyperclip.copy(detail_found.email)


    def delete_user(self):
        '''
        delete_credentials method deletes a saved contact from the contact_list
        '''
        userAccount.user_details.remove(self)

    @classmethod
    def display_user(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_details



class userCredentials:
    """
    Class that generates new instances of a userCredentials
    """

    user_credentials=[]

    def __init__(self,username,email,number,password):

            '''
            __init__ method that helps us define properties for our objects.

            self.username = username
            self.password = password
            self.number=number
            '''

            self.username=username
            self.email=email
            self.number=number
            self.password=password

    def save_credential(self):
        userCredentials.user_credentials.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved contact from the contact_list
        '''
        userCredentials.user_credentials.remove(self)


    # @classmethod
    # def find_by_number(cls,number):
    #     '''
    #     Method that takes in a usename and returns a contact that matches that number.

    #     Args:
    #         username: username to search for
    #     Returns :
    #         credentials.
    #     '''

    #     for credential in cls.user_credentials:
    #         if credential.number == number:
    #             return credential

    # @classmethod
    # def credential_exists(cls,number):
    #     '''
    #     Method that checks if a contact exists from the contact list.
    #     Args:
    #         number: Phone number to search if it exists
    #     Returns :
    #         Boolean: True or false depending if the contact exists
    #     '''
    #     for credential in cls.user_credentials:
    #         if credential.number == number:
    #             return True

    #     return False
                
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