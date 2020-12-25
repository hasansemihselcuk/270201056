password = "abc123"
a = 3

while a != 0 :
  u_password = input("Please enter the password :")
  if u_password == password :
    print("You have successfully logged in")
    break
  elif u_password != password:
    print("Sorry, the password is wrong")
    a=a-1
  if a ==0:  
    print("You have been denied access")
    break

