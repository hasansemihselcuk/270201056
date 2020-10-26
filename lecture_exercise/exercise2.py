h = 60
leave_home = 6*h + 52 
easy_pace = 8
tempo = 6 

running = (1* easy_pace) + (3 * tempo) + (2 * easy_pace)

total = leave_home + running

h2 = total // 60 
m2 = total % 60
print(h2,":" , m2,"am")

