
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