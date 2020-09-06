import unittest
from user import userAccount
from user import userCredentials
# from credentials import userCredentials
# from credentials import userCredentials


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):

        '''
            Set up method to run before each test cases.
        '''

        self.userDetails = userAccount("sylvia","mueni","0720670758","catherinekadogo001@gmail.com","KadogoKenya")

        # self.Credentials = userCredentials("KadogoKenya", "abcdef")

    def tearDown(self):

        '''
        tearDown method that does clean up after each test case has run.
        '''

        userAccount.user_details=[]


    def test_init(self):
        self.assertEqual(self.userDetails.first_name,"sylvia")
        self.assertEqual(self.userDetails.last_name,"mueni")
        self.assertEqual(self.userDetails.phone_number,"0720670758")
        self.assertEqual(self.userDetails.email,"catherinekadogo001@gmail.com")
        self.assertEqual(self.userDetails.user_name,"KadogoKenya")

        # self.assertEqual(self.Credentials.username,"KadogoKenya")
        # self.assertEqual(self.Credentials.username,"abcdef")

    def test_save_user(self):
        '''
        test_save_userDetails test case to test if the userAccount object is saved into
         the user list
        '''

        self.userDetails.save_user()
        self.assertEqual(len(userAccount.user_details),1)


   
    def test_save_multiple_Details(self):

        '''
        test_save_userDetails test case to test if the userAccount object is saved into
         the user list
        '''
        self.userDetails.save_user()
        self.new_userDetails = userAccount("Kat","Kanini","0711670758","catherine001@gmail.com","KenyaKenya")
        self.new_userDetails.save_user()
        self.assertEqual(len(userAccount.user_details),2)



class TestUserCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.credentials = userCredentials('KadogoKenya', 'abcdef') 


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        userCredentials.user_credentials=[]

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.credentials.username,'KadogoKenya')
        self.assertEqual(self.credentials.number,'0720670758')
        self.assertEqual(self.credentials.password,'abcdef')

    def test_save_credential(self):
        '''
        test_save_credentials test case to test if the contact object is saved into
        the credentials list
        '''
        self.credentials.save_credential() # saving the new created credentials
        self.assertEqual(len(userCredentials.user_credentials),1)

    def test_save_multiple_Credentials(self):
        '''
        test_save_credentials test case to test if the contact object is saved into
        the credentials list
        '''
        self.credentials.save_credential()
        self.new_credentials =userCredentials('Eliza','0711586438','ghijk')
        self.new_credentials.save_credential()
        self.assertEqual(len(userCredentials.user_credentials),2)


    def test_delete_credentials(self):
        self.credentials.save_credential()
        test_credential = userCredentials('kate','0711586438','ghijk')
        test_credential.save_credential()

        self.credentials.delete_credentials()
        self.assertEqual(len(userCredentials.user_credentials),1)

    def test_find_credentials_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''
        self.credentials.save_credential()
        test_credential = userCredentials('kate','0711586438','ghijk')
        test_credential.save_credential()

        found_credential = userCredentials.find_by_number('0711586438')

        self.assertEqual(found_credential.username,test_credential.username)

if __name__ == "__main__":
    unittest.main()

def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0711223344")

        self.assertEqual(found_contact.email,test_contact.email)