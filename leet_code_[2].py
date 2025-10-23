l1 = [2,4,3]
l2 = [5,6,4]

l3 = "".join(str(num) for num in l1)
l4 = "".join(str(num) for num in l2)
l5= int(l3)
l6 = int(l4)

l7 =l5+l6

l8 = [num for num in str(l7)][::-1]

print("sum 2 number: ",l5)
print("sum 2 number: ",l6)
print("sum 2 number: ",l7)
print("sum 2 number: ",l8)
