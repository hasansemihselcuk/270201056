first_number = int(input("first number:"))
second_number = int(input("second number:"))
same =0

while first_number > 0 and second_number > 0:
  if first_number % 10 == second_number % 10:
    same +=1
  
  first_number //=10 
  second_number //=10
print(same)