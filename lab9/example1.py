def harmonic(n):
  if n == 1 :
    return 1 
  elif n <=0 :
    return 0
  else:  
    
    
    return 1/n + harmonic(n-1)
a = int(input("n :"))
harmonic(a)
print(harmonic(a))