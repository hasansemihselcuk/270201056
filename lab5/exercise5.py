many=int(input("How many Fibonacci numbers will I generate for the user?: "))
a=1
b=1

fib_list=[a,b]
for i in range(many-2) :
  c=a+b
  fib_list.append(c)
  (c,a)=(a,c)
  (b,c)=(c,b)
print(fib_list)
