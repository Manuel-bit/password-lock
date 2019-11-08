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



if __name__ == "__main__":
  unittest.main()

