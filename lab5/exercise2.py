x= (int(input("How many numbers?")))
true = 0
for i in range(x):
  a=(int(input("Enter a integers?")))
  if a % 2 ==0:
    true += 1

print("%",(true / x )* 100)


  