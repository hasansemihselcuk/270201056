a ="10010"
c= 0
counter = -1
for i  in a[::-1] :
  counter += 1
  if i== "1" :
    b =2**counter
    c= c + b
    print(",,,,",c)

print(c)


