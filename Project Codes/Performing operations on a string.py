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


