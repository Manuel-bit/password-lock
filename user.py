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
