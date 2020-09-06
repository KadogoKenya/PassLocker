class userAccount:
    """
    Class that generates new instances of a userAccounts
    """


    # contact_list = []

    user_details=[]

    def __init__(self,first_name,last_name,phone_number,email,user_name,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New contact first name.
            first_name: New contact last name.
            number: New contact phone number.
            email : New contact email address.
            user_name : New contact user name.

        '''
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.user_name=user_name
        self.password=password

    def save_user(self):
        userAccount.user_details.append(self)
