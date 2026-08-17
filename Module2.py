
#Conditional Statements
# marks = 45
# if marks>=40:
#     print("Pass")
# else:
#     print("Fail")

# Output:
# Pass



#Important Operators used in Conditions

#1 Comparison operator
# a = 10
# b = 5
# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)

# Output:
# True
# False
# False
# True


#2 Logical Operator
# age = 20
# marks = 75
# print(age >= 18 and marks >= 60)
# print(age >= 18 or marks >= 90)
# print(not(age >= 18))

# Output:
# True
# True
# False



#Indentation in Conditional Statement

#Correct indentation
# age = 18
# if age >= 18:
#     print("Eligible for vote")

# Output: Eligible for vote

#Wrong indentation
# age = 18
# if age>=18:
# print("Eligible for vote")

# Output:
# It gives IndentationError



#if-statement

#syntax
# if condition:
#     statements

#Example
# age = 20
# if age >= 18:
#     print("You are eligible to vote")

# Output:
# You are eligible to vote



#if-else statement

#syntax
# if condition:
#     statements
# else:
#     statements

#Example
# num = 8
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# Output:
# Even number



#if-elif-else statement

#syntax
# if condition1:
#     statements
# elif condition2:
#     statements
# elif condition3:
#     statements
# else:
#     statements

#Example
# marks = 82
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 60:
#     print("Grade C")
# elif marks >= 40:
#     print("Grade D")
# else:
#     print("Fail")

# Output:
# Grade B



#Nested if statement

#syntax
# if condition1:
#     if condition2:
#         statements
#     else:
#         statements
# else:
#     statements

#Example
# age = 20
# has_voter_id = True
# if age >= 18:
#     if has_voter_id:
#         print("You can vote")
#     else:
#         print("You need voter ID")
# else:
#     print("You are not eligible to vote")

# Output:
# You can vote



#Short-hand if
#Example
# age = 20
# if age >= 18 : print("Eligible")
# Output:
# Eligible


#Short-hand if-else / Ternary operator

#syntax
# value_if_true if condition else value_if_false

#Example
# num = 7
# result = "Even" if num % 2 == 0 else "Odd"
# print(result)

# Output:
# Odd



#Using logical operator in conditions

#1 and operator
# age = 22
# marks = 70
# if age >= 18 and marks >= 60:
#     print("Eligible for interview")
# else:
#     print("Not eligible")

# output:
# Eligible for interview


#2 or operator
# day = "Sunday"
# if day == "Saturday" or day == "Sunday":
#     print("Weekend")
# else:
#     print("Working day")

# output:
# Weekend


#3 not operator
# is_raining = False
# if not is_raining:
#     print("You can go outside")
# else:
#     print("Take an umbrella")

# output:
# You can go outside



#Real-life programs using conditional statements

#1 Greatest of two number
# a = 25
# b = 40
# if a > b:
#     print("a is greater")
# else:
#     print("b is greater")

# output:
# b is greater


#2 Greatest of three number
# a = 10
# b = 25
# c = 15
# if a >= b and a >= c:
#     print("a is greater")
# elif b >= a and b >= c:
#     print("b is greater")
# else:
#     print("c is greater")

# output:
# b is greater


#3 Simple calculator
# a = 10 
# b = 5
# operator = "+"
# if operator == "+":
#     print(a + b)
# elif operator == "-":
#     print(a - b)
# elif operator == "*":
#     print(a * b)
# elif operator == "/":
#     print(a / b)
# else:
#     print("Invalid operator")

# output:
# 15


#4 Discount calculator
# amount = 6000

# if amount >= 5000:
#     discount = amount * 0.10
# else:
#     discount = amount * 0.05

# final_amount = amount - discount
# print("Discount:" , discount)
# print("Final Amount:" , final_amount)

# output:
# Discount: 600.0
# Final Amount: 5400.0


#5 Traffic signal
# signal = "red"
# if signal == "red":
#     print("Stop")
# elif signal == "yellow":
#     print("Get ready")
# elif signal == "green":
#     print("Go")
# else:
#     print("Invalid signal")

# output:
# Stop