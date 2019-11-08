class Credentials:
  credentials_list = []
  '''
  class that defines the credentials blueprint
  '''
  def __init__(self,appName,appPassword):
    self.appName = appName
    self.appPassword = appPassword


  def save_credential(self):
    Credentials.credentials_list.append(self)

  def delete_credential(self):
    '''
    frunction that enables a user to delete a credential
    '''
    Credentials.credentials_list.remove(self)

