import unittest
from user import userAccount
# from credentials import userCredentials
# from credentials import userCredentials


class TestContact(unittest.TestCase):

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

        self.userDetails = userAccount("sylvia","mueni","0720670758","catherinekadogo001@gmail.com","KadogoKenya", "abcdef")

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
        self.assertEqual(self.userDetails.password," ")


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
        self.new_userDetails = userAccount("Kat","Kanini","0711670758","catherine001@gmail.com","KenyaKenya"," ")
        self.new_userDetails.save_user()
        self.assertEqual(len(userAccount.user_details),2)

if __name__ == "__main__":
    unittest.main()
