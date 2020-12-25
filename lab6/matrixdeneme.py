n = int(input("n?"))
matrix=[]
for a in range(n):
  matrixa=[]
  for b in range(n):
    matrixa.append(0)
  matrix.append(matrixa)  
for i in range(n):
  print(matrix[i])
