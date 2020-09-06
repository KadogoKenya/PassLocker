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
    
    def __init__(self,username,password):

            '''
            __init__ method that helps us define properties for our objects.

            Args:
                first_name: New contact new password.
                last_name : New contact existing_password.
            
            '''
            self.username = username
            self.password = password

    def save_credential(self):
        userCredentials.user_credentials.append(self)

