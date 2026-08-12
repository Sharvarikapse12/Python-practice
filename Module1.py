
#Variables in Python
#Example
# name = "Rahul"
# age = 21
# marks = 85.5

# print(name)
# print(age)
# print(marks)

#Output : 
# Rahul
# 21
# 85.5


#Number Data Type

#int
# age = 21
# print(type(age))

#Output:
#<class 'int'>


#float
# price = 95.50
# print(type(price))

#Output:
# <class 'float'



#complex
# num = 2 + 3j
# print(type(num))

# Output:
# <class 'complex'



#String Datatype
# name = "Rahul"
# course = "Python"
# message = "Welcome to Python class"
# print(name)
# print(course)
# print(message)

# Output:
# Rahul
# Python
# Welcome to Python class


#Boolean Data Type
# is_pass = True
# is_failed = False
# print(type(is_pass))

# Output:
# <class 'bool'>

#Boolean values are mostly used in conditions and comparisons
# Example:
# age = 20
# print(age>=18)
# Output: True


#NoneType
# result = None
# print(result)
# print(type(result))

# #Output:
# None
# <class 'NoneType'>



#isistance()Function
# x = 10
# print(isinstance(x,int))
# print(isinstance(x,str))

# Output:
# True
# False


# Input() Function
# name = input("Enter your name:")
# print("Your name is" , name)

# Output:
# Enter your name:sharvari
# Your name is sharvari




#Type Conversion

#Implicit Type Conversion
# a = 10
# b = 2.5
# result = a + b
# print(result)
# print(type(result))

# Output:
# 12.5
# <class 'float'>


#Explicit Type Conversion
# x = "10"
# y = int(x)
# print(y + 5)

# Output:
# 15



#Operators In Python

#Arithmetic Operator
# a = 10
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# Output:
# 13
# 7
# 30
# 3.3333333333333335
# 3
# 1
# 1000


#Assignment Operator
# x = 10 
# x += 5
# print(x)

# Output:
# 15


#Comparison Operator
# a = 10
# b = 5
# print(a == b)
# print(a != b)
# print(a > b)

# Output:
# False
# True
# True


#Logical Operator
# age = 20
# marks = 80
# print(age >= 18 and marks >= 50)
# print(age >= 18 or marks < 50)
# print(not age >= 18)

# Output:
# True
# True
# False


#Bitwise Operator
# a = 5  #Binary:0101
# b = 3  #Binary:0011
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(a << 1)
# print(a >> 1)

# #Output:
# 1
# 7
# 6
# 10
# 2


#Membership Operator
# name = "Python"
# print("P" in name)
# print("z" not in name)

# Output:
# True
# True


#Identity Operator
# a = [10 , 20]
# b = a
# c = [10 , 20]
# print(a is b)
# print(a is c)
# print(a == b)

# Output:
# True
# False
# True


#Operator Precedence
# result = 10 + 5 * 2
# print(result)

# Output:
# 20


# result = (10 + 5) * 2
# print(result)

# Output:
# 30



#Solved Practice Programs

#Add Two Numbers
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# sum_value = a + b
# print("Sum:" , sum_value)

#Output:
# Enter first number:10
# Enter second number:20
# Sum:30


#Calculate Area Of Rectangle
# length = float(input("Enter length:"))
# breadth = float(input("Enter breadth:"))
# area = length * breadth
# print("Area of rectangle:" , area)

# Output:
# Enter length:10
# Enter breadth:20.5
# Area of rectangle:205.0


#Swap Two Numbers
# a = 10
# b = 20
# a,b = b,a
# print("a:" ,a)
# print("b:" , b)

# Output:
# a: 20
# b: 10


#Calculate Simple Interest
# principal = float(input("Enter principal amount:"))
# rate = float(input("Enter rate:"))
# time = float(input("Enter time:"))
# simple_interest = (principal * rate * time) / 100
# print("Simple Interest:" , simple_interest)

# Output:
# Enter principal:2500
# Enter rate:40
# Enter time:60
# Simple Interest:60000.0


#Check Type User Input
# value = input("Enter any value:")
# print("Value:" , value)
# print("Type:" , type(value))

# Output:
# Value:20
# Type: <class 'str'>




#Practice Problems

#1 To print name age and city
# name = input("Enter your name:")
# age = input("Enter your age:")
# city = input("Enter your city:")
# print(name)
# print(age)
# print(city)

# Output:
# Enter your name:sharvari
# Enter your age:20
# Enter your city:Nagpur
# sharvari
# 20
# Nagpur


#2 To add two numbers by users
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# print(a + b)

# Output:
# Enter first number:20
# Enter second number:30
# 50


#3 To calculate percentage of student
# total = 500
# marks = 400
# percentage = (marks / total) * 100
# print("Percentage of student:" , percentage)

# Output:
# Percentage of student: 80.0


#4 To calcute area of circle
# radius = float(input("Enter radius:"))
# area = 3.14 * radius**2
# print("Area of circle:" , area)

# Output:
# Enter radius:5
# Area of circle: 78.5


#5 To convert temp from celcius to fahrenheit
# celcius = 30
# fahrenheit = (celcius * 9 / 5) +32
# print("Conversion of celcius into Fahrenheit:" , fahrenheit)

# Output:
# Conversion of celcius into Fahrenheit: 86.0


#6 To swap 2 numbers
# a = 10
# b = 20
# a , b = b , a
# print("a:" , a)
# print("b:" , b)

# Output:
# a: 20
# b: 10


#7 To calculate simple interest
# principal = float(input("Enter principal amount:"))
# rate = float(input("Enter rate amount:"))
# time = float(input("Enter time:"))
# simple_interest = (principal*rate*time)/100
# print("Simple interest:" , simple_interest)

# Output:
# Enter principal amount:25000
# Enter rate amount:40
# Enter time:60
# Simple interest: 600000.0


#8 To take name and marks as input and print using f-string
# name = input("Enter your name:")
# marks = int(input("Enter your marks:"))
# print(f"My name is {name} and my marks is {marks}")

# Output:
# Enter your name:sharvari
# Enter your marks:90
# My name is sharvari and my marks is 90


#9 To check type of different variables
# name = "sharvari"
# age = 20
# is_pass = True
# result = None
# # print(type(name))
# print(type(age))
# print(type(is_pass))
# print(type(result))

# Output:
# <class 'str'>
# <class 'int'>
# <class 'bool'>
# <class 'NoneType'>