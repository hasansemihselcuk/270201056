years = int(input("years:"))

if years % 400 == 0 :
  print("leap years")
elif years % 100 == 0 :
  print("not leap years")
elif years % 4 == 0 :
  print("leap years")
else :
  print ("not leap years")