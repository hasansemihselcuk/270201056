
fe = "+2x-2y+5+4y=+18-1x"
fe1= fe.split("=")
print(fe)
ne = []
ne1= []
ne2=[]
ne3 = []
for i in fe1:
  ayırma = i.replace("+","/+")
  ne.append(ayırma)
print(ne)
for i in ne:
  ayırma = i.replace("-","/-")
  ne3.append(ayırma)
print(ne3)

f_p = ne3[0].split("/")
f_p.remove('')
s_p = ne3[1].split("/")
s_p.remove('')
print(f_p)
print(s_p)
f_p_a = []
f_p_b = []
f_p_c = []
for i in f_p:
  if 'x' in i:
    f_p_a.append(i)
  elif'y' in i:
    f_p_b.append(i)
  else:
    f_p_c.append(i)     
print(f_p_a)
print(f_p_b)
print(f_p_c)
print("------------")
s_p_a = []
s_p_b = []
s_p_c = []
#işaret değişimi
s_p2= []
for i in s_p:
  if '-' in i:
    i_change = i.replace("-","+")
    s_p2.append(i_change)
  elif '+' in i:
    i_change = i.replace("+","-")
    s_p2.append(i_change)
  print(s_p2)
#2. tarafta işaretsizse??
for i in s_p2:
  if 'x' in i:
    s_p_a.append(i)
  elif'y' in i:
    s_p_b.append(i)
  else:
    s_p_c.append(i)     
print(s_p_a)
print(s_p_b)
print(s_p_c)
print("---------")
fe_a= f_p_a  + s_p_a  #*x leri silcez
fe_b= f_p_b  + s_p_b
fe_c= f_p_c  + s_p_c
print(fe_a)
print(fe_b)
print(fe_c)
print("-----a kısmı------")
a=[]
for i in fe_a:
  fe_a = i.split("x")
  print(fe_a)
  #fe_a.remove('')
  a.append(fe_a[0])
  print(fe_a)
print(fe_a)
print(a)
at= int(a[0])+ int(a[1])
print(at)
print("--b kısmı-- ok -")
b=[]
for i in fe_b:
  fe_b = i.split("y")
  #fe_b.remove('') 
  b.append(fe_b[0])
  print(fe_b)
print(fe_b)
print(b)
bt = int(b[0]) + int(b[1])
print(bt)
print("-----c kısmı------")
c=[]

ct = int(fe_c[0])+int(fe_c[1])
print(ct)
print("Equations in the simplified form:")
print("{0}x+{1}y={2}".format(at,bt,-ct))
#3x+2y=13

