a= 2
b= 6 
c= -20

x1 = (-b + ((b**2 - 4*a*c)**0.5))/(2*a)
x2 = (-b - ((b**2 - 4*a*c)**0.5))/(2*a)


ex1= a*(x1**2) + b*x1 + c
ex2= a*(x2**2) + b*x2 + c



print("first root=",x1)
print("second root=",x2)