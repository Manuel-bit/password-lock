import unittest
from credentials import Credentials

class credentials_test(unittest.TestCase):
  '''
  class that defines testcase for credentials class
  '''
  def setUp(self):
    self.new_credential = Credentials("instagram","insta")

  def test_init(self):
    '''
    test init tests if credentials object has been instantiated correctly
    '''
    self.assertEqual(self.new_credential.appName, "instagram")
    self.assertEqual(self.new_credential.appPassword, "insta")

  def tearDown(self):
    '''
    tearDown does a clean up after every test has run
    '''
    Credentials.credentials_list=[]

  def test_save_credential(self):
    '''
    test_save_credentials tests if credentials object has been saved correctly
    '''
    self.new_credential.save_credential()

  def test_save_multiple_credentials(self):
    '''
    test_save_multiple_credentials test if we can save more than one credential
    '''
    self.new_credential.save_credential()
    test_credential = Credentials("facebook","face")
    test_credential.save_credential()
    self.assertEqual(len(Credentials.credentials_list),2)

  def test_delete_credentials(self):
    '''
    test_delete_credentials tests if we can delete a credential
    '''
    self.new_credential.save_credential()
    test_credential = Credentials("facebook","face")
    test_credential.save_credential()
    self.new_credential.delete_credential()
    self.assertEqual(len(Credentials.credentials_list),1)

  



if __name__ == "__main__":
  unittest.main()

