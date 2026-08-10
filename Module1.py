
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