gpa= float(input("Your's GPA:"))
number_of_lectures = int (input("Number of Lectures:"))

if gpa >= 2.0 and number_of_lectures >= 47 :
  print("GRADUATED!!!")
elif  gpa <= 2.0 and number_of_lectures >= 47 :
  print("Not enough GPA!")
elif  gpa >= 2.0 and number_of_lectures <= 47 :
  print("Not enough number of lectures!")
elif gpa <= 2.0 and number_of_lectures <= 47 :
  print("Not enough number of lectures and GPA!")
else :
  print("Doğru sayıları gir")