x = eval(input("please write first number"))
y = eval(input("please write second number"))
z = eval(input("please write third number"))

if x<=y<z :
  print (x)
elif x<=z<y:
  print (x)
elif y<=x<z or y<=z<x :
  print(y)
else:
  print(z)
