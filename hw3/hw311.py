def f1():
  f = open("users.txt", "r")
  satır=[]
  satır=(f.readlines())
  for i in range(len(satır)):
    satır[i]=satır[i].split(";")
  i1 = "*"
  for i in range(len(satır)):
    if user == satır[i][0]:
      i1 = i
    elif i1 != "*":
      pass
    else :
      i1 = "*"
  
  i2 ="^"
  for i in range(len(satır)):
    if password == satır[i][1]:
      i2 = i
    elif i2 != "*":
      pass  
    else:
      i2 ="^"
  if i1 == i2 :
    confirmed = i1 #kim olduğunu bilmek için
    #login = "+"
    print("Logged in\n")
  elif i1 == "*" or i2 == "^":
    confirmed = 3549
    #login = "-"
    print("Wrong password or username\n")
  return confirmed 

user= input("Please enter username:\n")
password = input("Please enter password:\n")



print(type(f1()))
"""
ahmet;4567;ayse
ovgu;6789;
ayse;5678;ali,ahmet
ali;1234;ahmet,ovgu,ayse
"""