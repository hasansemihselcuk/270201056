m1=  [[3 ,2 ,6],
     [10, 6, 4],
     [5, 1 ,-4]]
n = int(input("n? "))
for i in range(n):
  m1 = int(input("items ?"))
  






sums= 0
for i in range(len(m1)):
 sums = sums + m1[i][i]
 print(m1[i])
print(sums)