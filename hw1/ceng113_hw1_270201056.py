fe1= input("Enter the first equation:\n")
fe2= input("Enter the second equation:\n")
fes = []
fes.append(fe1)
fes.append(fe2)
f1a=[]
f2a=[]
f3a=[]
for i in range(2):
  fe = fes[i]
  fe1= fe.split("=")
  ne = []
  ne1 = []
  for i in fe1:
    ayırma = i.replace("+","/+")
    ne.append(ayırma)
  for i in ne:
    ayırma = i.replace("-","/-")
    ne1.append(ayırma)
  f_p = ne1[0].split("/")
  f_p.remove('')
  s_p = ne1[1].split("/")
  f_p_a = []
  f_p_b = []
  f_p_c = []
  f_p_x_c = 0
  f_p_y_c = 0
  f_p_c_c = 0
  for i in f_p:
    if 'x' in i:
      f_p_a.append(i)
      f_p_x_c +=1
    elif'y' in i:
      f_p_b.append(i)
      f_p_y_c +=1
    else:
      f_p_c.append(i)
      f_p_c_c +=1     
  s_p_a = []
  s_p_b = []
  s_p_c = []
  s_p_x_c = 0
  s_p_y_c = 0
  s_p_c_c = 0
  s_p2= []
  for i in s_p:
    if '-' in i:
      i_change = i.replace("-","+")
      s_p2.append(i_change)
    elif '+' in i:
      i_change = i.replace("+","-")
      s_p2.append(i_change)
  for i in s_p2:
    if 'x' in i:
      s_p_a.append(i)
      s_p_x_c +=1
    elif'y' in i:
      s_p_b.append(i)
      s_p_y_c +=1
    else:
      s_p_c.append(i)
      s_p_c_c +=1     
  fe_a= f_p_a  + s_p_a 
  fe_x_c = f_p_x_c +s_p_x_c 
  fe_b= f_p_b  + s_p_b
  fe_y_c = f_p_y_c +s_p_y_c 
  fe_c= f_p_c  + s_p_c
  fe_c_c = f_p_c_c +s_p_c_c 
  a=[]
  for i in fe_a:
    fe_a = i.split("x")
    a.append(fe_a[0])
  at=0
  for i in range(fe_x_c):
    at += int(a[i])
  b=[]
  for i in fe_b:
    fe_b = i.split("y")
    b.append(fe_b[0])
  bt=0
  for i in range(fe_y_c):
    bt += int(b[i])
  c=[]
  ct=0
  for i in range(fe_x_c):
    ct += int(fe_c[i])
  f1a.append(at)
  f2a.append(bt)
  f3a.append(ct)
print("Equations in the simplified form:")
for i in range(2):
  if int(f2a[i])>= 0 :
    print("{0}x+{1}y={2}".format(f1a[i],f2a[i],-f3a[i]))
  else:
    print("{0}x{1}y={2}".format(f1a[i],f2a[i],-f3a[i]))
print("Solution:")
if f1a[0] != 0 :
  y = ((-f3a[1]*f1a[0])-(f1a[1]*-f3a[0]))/((f1a[0]*f2a[1])-(f2a[0]*f1a[1]))
  x= ((-f3a[0]) -(f2a[0]*y))/f1a[0]
  print("x="+str(int(x)))
  print("y="+str(int(y)))
elif f1a[0] == 0 :
  y = -f3a[0]/f2a[0]
  x = (-f3a[1]/f1a[1]) - ((f2a[1]*-f3a[0])/(f2a[0]*f1a[1]))
  print("x="+str(int(x)))
  print("y="+str(int(y)))