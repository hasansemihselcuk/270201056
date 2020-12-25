print("<<<<<<<<----s.e------->>>>>>>>")
fe = "-10y+5x-4y+10y=+7"
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
print(f_p_a)
print(f_p_b)
print(f_p_c)
print("f_p x adedi",f_p_x_c,"  y adedi",f_p_y_c,"  c adedi",f_p_c_c)
print("------------")
s_p_a = []
s_p_b = []
s_p_c = []
s_p_x_c = 0
s_p_y_c = 0
s_p_c_c = 0
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
    s_p_x_c +=1
  elif'y' in i:
    s_p_b.append(i)
    s_p_y_c +=1
  else:
    s_p_c.append(i)
    s_p_c_c +=1     
print(s_p_a)
print(s_p_b)
print(s_p_c)
print("s_p x adedi",s_p_x_c,"  y adedi",s_p_y_c,"  c adedi",s_p_c_c)
print("---------")
fe_a= f_p_a  + s_p_a 
fe_x_c = f_p_x_c +s_p_x_c 
fe_b= f_p_b  + s_p_b
fe_y_c = f_p_y_c +s_p_y_c 
fe_c= f_p_c  + s_p_c
fe_c_c = f_p_c_c +s_p_c_c 
print(fe_a)
print(fe_b)
print(fe_c)
print("fe x adedi",fe_x_c,"  y adedi",fe_y_c,"  c adedi",fe_c_c)
print("-----a kısmı kadar sorunsuz------")
a=[]
for i in fe_a:
  fe_a = i.split("x")
  print(fe_a)
  #fe_a.remove('')
  a.append(fe_a[0])
  print(fe_a)
print(fe_a)
print(a)
at=0
for i in range(fe_x_c):
  at += int(a[i])
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
bt=0
for i in range(fe_y_c):
  bt += int(b[i])
print(bt)
print("-----c kısmı------")
c=[]

ct=0
for i in range(fe_x_c):
  ct += int(fe_c[i])

print(ct)
print("Equations in the simplified form:")
if bt> 0 :
  print("{0}x+{1}y={2}".format(at,bt,-ct))
else:
  print("{0}x{1}y={2}".format(at,bt,-ct))
#5x-4y=7
