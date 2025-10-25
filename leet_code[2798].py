hours =[0,3,45,6,7,8]
target = 2

number_emp = 0

for hr in hours:
    if hr >= target:
        number_emp = number_emp + 1
print(number_emp)
#return number_emp