mlist = [1, 2, 3, 4]
#a = list(input("liste :"))
newlist= []
def get_list(a: list):
  for i in range(len(a)):
    newlist.append(a[ (len(a)-1 -i)])
  return newlist
    
get_list(mlist)
print(newlist)

""""
3 0
2 1 
1 2 
0 3
"""