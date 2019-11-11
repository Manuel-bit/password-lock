import random
import string
import pyperclip
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

  @classmethod
  def find_by_app_name(cls,appName):
    '''
    method that takes in application name and returns its details
    '''
    for credentials in cls.credentials_list:
      if credentials.appName == appName:
        return credentials

  @classmethod
  def display_credentials(cls):
    '''
    method tha returns a list of all credentials
    '''
    return cls.credentials_list

  @classmethod
  def generate_password(cls):
    '''
    method that generates password
    '''
    password = string.ascii_lowercase
    return "".join(random.choice(password)for i in range (10))

  @classmethod
  def coppy(cls,appName):
    found_app = Credentials.find_by_app_name(appName)
    pyperclip.copy(found_app.appName)


