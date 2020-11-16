number = int(input("number:"))

if number < 10:
  result = "0" + str(number)
else:
  first_digit = number % 10 
  second_digit = (number// 10) % 10
  result = str(second_digit)+ str(first_digit)


print(result)