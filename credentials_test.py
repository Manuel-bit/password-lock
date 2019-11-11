import unittest
from credentials import Credentials
import random
import string
import pyperclip

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

  def find_by_app_name(self):
    '''
    test that checks if we can search for an app by app name
    '''
    self.new_credential.save_credential()
    test_credential = Credentials("facebook","face")
    test_credential.save_credential()

    found_credential = Credentials.find_by_app_name("facebook")
    self.assertEqual(found_credential.app_Name,test_credential.appName)

  def test_display_all_details(self):
    '''
    method tha returns credentials_list
    '''
    self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

  def test_generate_password(self):
    '''
    test that checks if password is generated correctly
    '''
    password = string.ascii_lowercase
    return "".join(random.choice(password)for i in range(10))
    self.assertTrue(len(password) > 0)

  def test_coppy_name(self):
    '''
    test to confirm we can coppy appName
    '''
    self.new_credential.save_credential()
    test_credential = Credentials("facebook","face")
    test_credential.save_credential()
    Credentials.coppy("facebook")

    self.assertEqual(test_credential.appName, pyperclip.paste())






  



if __name__ == "__main__":
  unittest.main()

