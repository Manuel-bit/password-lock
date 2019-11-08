import unittest
from user import User

class testUser(unittest.TestCase):
  '''
  class that defines test case for user class
  '''
  def setUp(self):
    '''
    set up method runs before evry testcase
    '''
    self.new_user = User("manu", "lilfranken", "enjuguna26@gmail.com")


  def test_init(self):
    '''
    test init tests whether an object is initialised correctly
    '''
    self.assertEqual(self.new_user.username,"manu")
    self.assertEqual(self.new_user.password,"lilfranken")
    self.assertEqual(self.new_user.email,"enjuguna26@gmail.com")

  def tearDown(self):
    '''
    tearDown does a clean up after evry test has run
    '''
    User.user_list =[]


  def test_save_user(self):
    '''
    test_save_user test whether user objects are saved to the user_list
    '''
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)

  def test_save_multiple_user(self):
    '''
    test_save_multiple_user tests whether the program can save more than one user
    '''
    self.new_user.save_user()
    test_user = User("john","doe","johndoe@gmail.com")
    test_user.save_user()
    self.assertEqual(len(User.user_list),2)

  def test_find_user_by_name(self):
    '''
    test_find_user_by_name tests if we can search for user by username
    '''
    self.new_user.save_user()
    test_user = User("john","doe","johndoe@gmail.com")
    test_user.save_user()
    found_user = User.find_by_name("test")
    self.assertEqual(found_user.email,test_user.email)

if __name__ == "__main__":
  unittest.main()




  

  
    

  


















  


  



