fe= "+2x-2y+5+4y=+18-1x"
print(type(fe))
x_loc = []
y_loc = []

fe_list = []
for i in fe:
  fe_list.append([i])
print(fe_list)
x_c = fe_list.count(['x'])
for a in range(x_c):
  x_i = fe_list.index(['x'])
  x_loc.append(x_i+a)
  fe_list.remove(fe_list[x_i])
print(fe_list)

fe_list = []
for i in fe:
  fe_list.append([i])
print(fe_list)
y_c = fe_list.count(['y'])
for a in range(y_c):
  y_i = fe_list.index(['y'])
  y_loc.append(y_i+a)
  fe_list.remove(fe_list[y_i])
print(x_loc , "/", y_loc) # indexleri
print(fe_list)

for a in range(x_c):
  x_i = fe_list.index(['x'])
  fe_list.remove(fe_list[x_i])
print(fe_list)

# her şeyin indexinden gitçem a nında falan sonra a ları topla = den büyükse indeks - leri ile vs.

""""
for i in ne1:
  ayırma = i.replace("x","*x")
  ne2.append(ayırma)
print(ne2)
for i in ne2:
  ayırma = i.replace("y","*y")
  ne3.append(ayırma)
print(ne3)
"""