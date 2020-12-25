def func(a):
  for i in range(2,a):
    if a% i == 0:
      print("not prime")
      break
  print("prime number")

n1 = int(input("number 1:"))

func(n1)
