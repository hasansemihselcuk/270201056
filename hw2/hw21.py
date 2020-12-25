provinces = open("provinces.txt","r")
all_provinces = provinces.readlines()
n_provinces=[]
x_provinces=[]
y_provinces=[]
n_provinces_alphabetic=[]

for a in range(81):
  all_provinces[a]=all_provinces[a].split(",")
  n_provinces.append(all_provinces[a][0])
  n_provinces_alphabetic.append(all_provinces[a][0])
n_provinces_alphabetic.sort(reverse=False)

print(n_provinces)
print(n_provinces_alphabetic)
p1="ANKARA"

#----part of determination departure province--------
while True:
  possible=[]
  possible2=[]
  Possible_provinces="a"
  p2 = input("Arrival province:\n")
  p2= p2.upper()
  if p2 == p1 :
      print("Enter a different province!")
      pass
  elif p2 in n_provinces:
    
    p2 = p2
    break
  
  else :
    print("Province not found!")
    for a in range(81):
      if p2 in n_provinces_alphabetic[a] :
        possible.append(n_provinces_alphabetic[a])   
    for i in range(len(possible)):      
      if p2 == possible[i][:len(p2)]:
        possible2.append(possible[i])
    Possible_provinces= Possible_provinces.replace("a",possible2[0])
    if len(possible2)==1 :
      print("Possible province:"+Possible_provinces)

    elif len(possible2)>=2 :    
      for c in range(1,(len(possible2))):
        Possible_provinces=Possible_provinces+","+ possible2[c]
      print("Possible provinces:"+Possible_provinces)