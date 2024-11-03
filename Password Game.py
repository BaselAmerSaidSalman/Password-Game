password = "basel"
password_input = input("Please enter your password: \n")
while password_input != password:
  print("Wrong password, please try again")
  password_input = input("Please enter your password: \n")
if password == password_input:
  print("Welcome back")

  