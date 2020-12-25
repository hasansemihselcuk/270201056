a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]

def func(a_list) :
  sums = 0
  for i in range(len(a_list)):
    sums = sums + a_list[i]
  return sums
sums = func(a_list)
print("Results: ",sums)

