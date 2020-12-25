file = open("members.txt","w")
file.write("Azad:azad@gmail.com\nHasan:hasan@email.com")
file = open("members.txt","r")
members_dic= {}


while True :
  line = file.readline()
  if line == "":
    break
  line = line.split(':')
   
  members_dic[line[0]]= line[1]
file.close()
print(members_dic)
