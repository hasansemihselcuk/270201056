p1= "abc123"
password = input("Enter Password: ")


while  (password != p1) :
  
  if (password == "help"):
    print(p1[0])
  else:
    print("wrong")
  password = input("Try again,Enter Password: ")

print("welcome")