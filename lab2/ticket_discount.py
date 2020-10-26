age = int(input("How old are you?"))
bus_ticket = 3 

if age < 6 or age>= 60 :
  print("Free")
elif  6 <= age <= 18 :
  print("%50 discount")
else :
  print("3 TL ")