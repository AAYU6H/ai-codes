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