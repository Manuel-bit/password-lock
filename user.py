class User:
  user_list =[]
  
  '''
  class that defines user blueprint
  '''
  def __init__(self,username,password,email):
    self.username = username
    self.password = password
    self.email = email

  def save_user(self):
    '''
    function that saves new user objects
    '''
    User.user_list.append(self)

  @classmethod
  def find_by_name(cls, username):
    '''
    method that takes in user name and finds the user that matches it
    '''
    for user in cls.user_list:
      if user.username == username:
        return user

