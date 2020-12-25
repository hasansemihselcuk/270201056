a = "abc1234567"
level = 0
if len(a) < 8 or " " in a :
  print("Level ",level)

level = 0
alfa= 0
alnum = 0
numeric=0
for i in (a):
  
  if i.isalpha()== True:
   alfa +=1
   level +=1
  elif i.isalnum() == True:
    level +=1
    alnum +=1
  elif i.isnumeric() == True:
    level +=1
    numeric+=1

print("level ",level+(- alfa - alnum - numeric)+3)
