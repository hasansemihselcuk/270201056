def f1():
  user= input("Please enter username:\n")
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
  password = input("Please enter password:\n")
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
  confirmed(confirmed)
  return confirmed


f1()
def confirmed(a):
  a = int(a)
  return a 

print(confirmed)
def f2():
  new_user_name = input("Please enter username:\n")
  f = open("users.txt", "r")
  satır=[]
  instants_users=[]
  satır=(f.readlines())
  for i in range(len(satır)):
    satır[i]=satır[i].split(";")
    instants_users.append(satır[i][0])
  f.close()
  if " " in new_user_name :
    uygun1 = "-"
    print("Username not valid\n")
  elif new_user_name in instants_users :
    uygun1= "-"
    print("Username not valid\n")
  elif new_user_name == new_user_name.lower() and new_user_name.isalnum()== True :
    uygun1 = "+"
  else:
    uygun1= "-"
    print("Username not valid\n")
  new_user_password = input("Please enter password:\n")
  if 4<=len(new_user_password)<=8 and new_user_password.isalnum()== True and new_user_password.isalpha()== False :
    uygun2 = "+"
  else :
    uygun2 = "-"
    print("Password not valid\n")
  if uygun1== "+" and uygun2 == "+":
  #ekleme
    new_user = []
    new_user.append(new_user_name +";"+ new_user_password+";\n")
    satır.append(new_user)
    b = []
    b1= " "
    for i in range(len(satır)-1):
      b.append(satır[i][0]+";"+satır[i][1]+";"+satır[i][2])
    b = b+(satır[-1])
    for i in range(len(b)):
      if b1 == " ":
        b1= b1.replace(" ",b[i])
      else:
        b1 = b1+ b[i]
    f = open("users.txt", "w")
    f.write(b1)
    f.close
  return new_user_name, new_user_password 

def f3(): 
  n_friend = input("Please enter the name of your new friend:\n")
  f = open("users.txt", "r")
  satır=[]
  instants_users=[]
  satır=(f.readlines())
  for i in range(len(satır)):
    satır[i]=satır[i].split(";")
    instants_users.append(satır[i][0])
  f.close()
  if n_friend in instants_users :
    print("found")
    new= ","+ n_friend+"\n"
    satır[confirmed][2]=(satır[confirmed][2].replace("\n",new)) 
    print(satır)
    b = []
    b1= " "
    for i in range(len(satır)):
      b.append(satır[i][0]+";"+satır[i][1]+";"+satır[i][2])
    for i in range(len(b)):
      if b1 == " ":
        b1= b1.replace(" ",b[i])
      else:
        b1 = b1+ b[i]
    f = open("users.txt", "w")
    f.write(b1)
    f.close
  else :
    print("Friend not found\n")
  

confirmed = 3

def f4():
  f = open("users.txt", "r")
  satır=[]
  satır=(f.readlines())
  f.close
  for i in range(len(satır)):
    satır[i]=satır[i].split(";")
  satır[confirmed][2]=satır[confirmed][2].replace("\n","")
  print(satır[confirmed][2])




""""
1. Log in / change user
2. Create new user
3. Add friend
4.Show my friends
5. Exit
"""
"""
ahmet;4567;ayse
ovgu;6789;
ayse;5678;ali,ahmet
ali;1234;ahmet,ovgu,ayse
"""