#Topic : Take 3 numbers as input and find the greatest number

x, y, z = input("Enter three values: ").split(",")

if (x >= y) and (x >= z):
   greatest = x
elif (y >= x) and (y >= z):
   greatest = y
else:
   greatest = z

print("Greatest of the three numbers = ", greatest)

