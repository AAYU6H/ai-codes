# Topic : Adding two integers

num1 = 84.5
num2 = 84.5
print("Integer 1 =", num1)
print("Integer 2 =", num2)
print("Sum of integers : ", int(num1 + num2))


# Topic : WAP to add any value to a given list by specific index position.

lst = ["Hello", "World", "This", "is", "Python"]
print(lst)

insertValue = "not"

print("After inserting a new value : ")
lst.insert(4, insertValue)
print(*lst)


#Topic : Take 3 numbers as input and find the greatest number

x, y, z = input("Enter three values: ").split(",")

if (x >= y) and (x >= z):
   greatest = x
elif (y >= z) and (y >= x):
   greatest = y
elif (z >= x) and (z >= y):
   greatest = z

print("Greatest of the three numbers = ", greatest)


#Topic : Take the length and width of a rectangle as input, and find its perimeter and area

print("Finding perimeter and area of a rectangle, by getting length and width as input from user")
length = float(input("Please enter the length of the rectangle : "))
width = float(input("Please enter the width of the rectangle : "))

perimtr = 2*(length+width)
area = length*width

print("Perimeter of the rectangle = ", perimtr)
print("Area of the rectangle = ", area)


"""
Write a program to perform the following operations on the given list:
('Orange', 'Mango', 'Papaya', 'Apple', 'Grapes')
a) Remove "Papaya" and add "Guava" at the same position.
b) Sort the list in ascending order.
d) Add the "Cherry, Banana, Coconut" to the list.
"""
fruits = ["Orange", "Mango", "Papaya", "Apple", "Grapes"]
print(fruits)

print("Replacing Items in the list")
fruits = ["Orange", "Mango", "Papaya", "Apple", "Grapes"]
target_index = fruits.index("Papaya")
fruits[target_index] = "Guava"
print(fruits)

#Sorting the list
print("Sorted List : ")
fruits.sort()
print(fruits)

#Adding more fruits
print("Adding more items to list : ")
moreFruits = ["Cherry", "Banana", "Coconut"]
fruits.extend(moreFruits)
print(fruits)


"""
Topic : Write a program to perform the following operations on the given string:
"Python is an interpreted, high-level and general-purpose programming language."
a) Find the length of the string.
b) Find the word "and" and replace it with symbol "&".
c) Join the string with the text "It has a simple syntax similar to the English language,
"""
sen = "Python is an interpreted, high-level and general-purpose programming language."

print("Length of the string : ", len(sen))

#Finding and replacing the words
print("Replacing 'and' with '&' : ")
senNew = sen.replace("and", "&")
print(senNew)

# Joining new string
print("Joining new string with existing string : ")
sen2 = "It has a simple syntax similar to the Enlish language."

print(sen + " " + sen2)



