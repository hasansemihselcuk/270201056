provinces = open("provinces.txt","r")
all_provinces = provinces.readlines()
n_provinces=[]
x_provinces=[]
y_provinces=[]
n_provinces_alphabetic=[]
for a in range(81):
  all_provinces[a]=all_provinces[a].split(",")
  n_provinces.append(all_provinces[a][0])
  x_provinces.append(all_provinces[a][1])
  y_provinces.append(all_provinces[a][2])
  y_provinces[a]=y_provinces[a].replace("\n","")
  n_provinces_alphabetic.append(all_provinces[a][0])
n_provinces_alphabetic.sort(reverse=False)
while True:
  possible=[]
  possible2=[]
  Possible_provinces="a"
  p1 = input("Departure province:\n")
  p1= p1.upper()
  if p1 in n_provinces:
    p1 = p1
    break
  else :
    print("Province not found!")
    for a in range(81):
      if p1 in n_provinces_alphabetic[a] :
        possible.append(n_provinces_alphabetic[a])   
    for i in range(len(possible)):      
      if p1 == possible[i][:len(p1)]:
        possible2.append(possible[i])    
    if len(possible2)==0 :      
      pass
    elif len(possible2)==1 :
      Possible_provinces= Possible_provinces.replace("a",possible2[0])
      print("Possible province:"+Possible_provinces)
    elif len(possible2)>=2 : 
      Possible_provinces= Possible_provinces.replace("a",possible2[0])   
      for c in range(1,(len(possible2))):
        Possible_provinces=Possible_provinces+","+ possible2[c]
      print("Possible provinces:"+Possible_provinces)
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
    if len(possible2)==0 :
      
      pass

    elif len(possible2)==1 :
      Possible_provinces= Possible_provinces.replace("a",possible2[0])
      print("Possible province:"+Possible_provinces)

    elif len(possible2)>=2 : 
      Possible_provinces= Possible_provinces.replace("a",possible2[0])   
      for c in range(1,(len(possible2))):
        Possible_provinces=Possible_provinces+","+ possible2[c]
      print("Possible provinces:"+Possible_provinces)
while True:
  T_T = input("Enter travel type:\n")
  T_T=T_T.upper()
  if T_T== "CAR" :
    T_T = 90
    t_type="CAR"
    break
  elif T_T == "MOTORCYCLE" :
    T_T = 80
    t_type="MOTORCYCLE"
    break
  elif T_T== "BICYCLE" :
    T_T = 25
    t_type="BICYCLE"
    break
n_p1 = n_provinces.index(p1)
n_p2 = n_provinces.index(p2)
dx = eval(x_provinces[n_p1])- eval(x_provinces[n_p2])
dy = eval(y_provinces[n_p1])- eval(y_provinces[n_p2])
distance= ((dx*dx)+ (dy*dy))**(1/2)
distance_km = distance *100
travel_time = distance_km/ T_T
hours = int(travel_time)
minutes=int((travel_time - hours)*60)
print("")
print("I am calculating the distance between {} and {} ...".format(p1,p2))
print("")
print("Distance:",round(distance_km,2),"km")
print("Approximate travel time with {}: {} hours {} minutes".format(t_type,hours,minutes))
distance_provices=[]
close_3_distance=[]
close_list=[]
for i in range(81):
  distance_provices.append(((eval(x_provinces[n_p1])-eval(x_provinces[i]))**2+ (eval(y_provinces[n_p1])-eval(y_provinces[i]))**2)**1/2)
distance_provices.sort(reverse=False)
close_3_distance.append(distance_provices[1])
close_3_distance.append(distance_provices[2])
close_3_distance.append(distance_provices[3])
distance_provices=[]
for i in range(81):
  distance_provices.append(((eval(x_provinces[n_p1])-eval(x_provinces[i]))**2+ (eval(y_provinces[n_p1])-eval(y_provinces[i]))**2)**1/2)
close_list.append(distance_provices.index(close_3_distance[0]))
close_list.append(distance_provices.index(close_3_distance[1]))
close_list.append(distance_provices.index(close_3_distance[2]))
close_list.sort()
print("Recommended places close to {}:".format(p1)+ n_provinces[(close_list[0])]+","+n_provinces[(close_list[1])]+","+n_provinces[(close_list[2])])