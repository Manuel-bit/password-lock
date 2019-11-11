from user import User
from credentials import Credentials
import sys

def create_user(username,password,email):
  '''
  function that creates new users
  '''
  new_user = User(username,password,email)
  return new_user

def create_credentials(appName,appPassword):
  '''
  function that creates new credentials
  '''
  new_credential = Credentials(appName,appPassword)
  return new_credential

def save_user(user):
  '''
  function that saves user object to user_list
  '''
  user.save_user()

def save_credentials(credentials):
  '''
  function that saves new credentials
  '''
  credentials.save_credential()

def delete_credentials(credentials):
  '''
  function that removes credentials from credentials_list
  '''
  credentials.delete_credential()

def find_user(username):
  '''
  function that takes in username and returns user
  '''
  return User.find_by_name(username)

def find_credentials(appName):
  '''
  function that returns application details
  '''
  return Credentials.find_by_app_name(appName)

def display_user():
  '''
  function that returns user list
  '''
  return User.display_user()

def display_credentials():
  '''
  function that returns credentials_list
  '''
  return Credentials.display_credentials()

def generate_password():
  '''
  function that generates random passwords
  '''
  return Credentials.generate_password()

def coppy_name(appName):
  '''
  finction that coppies app name
  '''
  return Credentials.coppy(appName)

def main():
  print("Hello, Welcome to password locker, what is your name? ")
  username = input()

  print(f" hello {username} , welcome to password locker, sign up to log in..")
  print('\n')

  print("Enter your  username....")
  logusername = input()

  print("Enter your password....")
  logpassword = input()

  print("Enter email....")
  email = input()
  print("\n")

  print("log in to your account now..")
  print('\n')

  print("enter your user name")
  username = input()

  print("enter password..")
  password = input()

  if logusername == username and logpassword == password:
    print("successfully loged in!!")
    print('\n')

  else:
    print("incorect password!!try again")
    sys.exit()

  while True:
    print("use these short codes : cc - create a new credential, dc - display credentials, del -delete credential,cc - coppy credential, ex - exit password locker")
    short_code = input()

    if short_code == 'cc':
      print("Create new credential")
      print("-"*10)

      appName = input("enter the application name: ")
      print("\n")
      ans = input("would you like password locker to generate you a password: (y/n):\t").lower()
      if ans == "n":
        password = ("enter password:\t")
      else:
        password = generate_password()

      save_credentials(create_credentials(appName,password))

      print('\n')
      print(f"New detail for {appName} created successfully")
      print('\n')

    elif short_code == "dc":
      if display_credentials:
        print("here is a list of all yor credentials:")
        print("-"*30)
        print('\n')
        for credentials in display_credentials():
          print(f"{credentials.appName} ---- {credentials.appPassword}")
          print('\n')

      else:
        print('\n')
        print("you do not seem to have any credentials or applications saved")

    elif short_code == "del":
      delete = input("enter name of app you want to delete ")
      if find_credentials(delete):
        to_delete = find_credentials(delete)
        delete_credentials(to_delete)

      else:
        print("{delete} is not in your details list")

    elif short_code == "cc":
      copy = input("enter app name to coppy: \t ")
      to_coppy = coppy_name(copy)
      print(to_coppy)

    elif short_code == "ex":
      sys.exit()

if __name__ == "__main__":
  main()








  


    





