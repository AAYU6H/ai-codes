#Topic : Take the length and width of a rectangle as input, and find its perimeter and area

print("Finding perimeter and area of a rectangle, by getting length and width as input from user")
length = float(input("Please enter the length of the rectangle : "))
width = float(input("Please enter the width of the rectangle : "))

perimtr = 2*(length+width)
area = length*width

print("Perimeter of the rectangle = ", perimtr)
print("Area of the rectangle = ", area)


