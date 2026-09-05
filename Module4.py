#String
#string is a sequence od character . In python, strings are written inside quotes , double quotes or triple quotes 

#Example
# name = "Python"
# message = 'Welcome'
# paragraph = """ This is a multi-line string."""
# print(name)
# print(message)

# output:
# Python
# Welcome


#String Indexing
# name = "Python"
# print(name[0])
# print(name[1])
# print(name[-1])

# output:
# P
# y
# n


#String Immutability
# name = "Python"
# name = "Jython"
# print(name)

# output:
# Jython


#String methods
#1 upper()
# 2 lower()
# 3 title()
# 4 strip()
# 5 replace() 
# 6 split()
# 7 join()
# 8 find()
# 9 count()
# 10 startswith()
# 11 endswith()

#Example of string method
# text = " python programming "
# print(text.upper())
# print(text.strip())
# print(text.replace("python" , "java"))
# print(text.count("p"))

# output:
#  PYTHON PROGRAMMING 
# python programming
#  java programming 
# 2


#String formatting
# name = "Rahul"
# marks = 85
# print(f"Student name is {name} and marks are {marks}")

# output:
# Student name is Rahul and marks are 85


#Escape character
# print("Hello\nPython")
# print("Name\tMarks")

# output:
# Hello
# Python
# Name    Marks


#Program: Reverse a string
# text = "python"
# reverse = text[::-1]
# print(reverse)

# output:
# nohtyp


#Program: Palindrome string
# text = "madam"
# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# output:
# Palindrome