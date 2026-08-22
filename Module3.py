#Loops & Types

#1 For loop
# for i in range (1 , 6):
#     print(i)

# output:
# 1                    
# 2
# 3
# 4
# 5


#Range function
# for i in range(2,11,2):
#     print(i)

# output:
# 2
# 4
# 6
# 8
# 10


#2 While loop
# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1

# output:
# 1
# 2
# 3
# 4
# 5


#break statement
# for i in range(1 , 10):
#     if i == 5:
#         break
#     print(i)

# output:
# 1
# 2
# 3
# 4


#continue statement
# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)

# output:
# 1
# 2
# 4
# 5


#Pass statement
# for i in range(1,4):
#     pass
# print("Loop completed")

# output:
# Loop completed


#3 Nested loop
# for i in range(1,4):
#     for j in range(1,14):
#         print(i,j)

# output:
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10
# 1 11
# 1 12
# 1 13
# 2 1
# 2 2
# 2 3
# 2 4
# 2 5
# 2 6
# 2 7
# 2 8
# 2 9
# 2 10
# 2 11
# 2 12
# 2 13
# 3 1
# 3 2
# 3 3
# 3 4
# 3 5
# 3 6
# 3 7
# 3 8
# 3 9
# 3 10
# 3 11
# 3 12
# 3 13


#Problem questions

#1 print num 1 to 100
# for i in range(1,101):
#     print(i)

# output:
# 1
# 2
# 3
# 4
# .
# .
# .
# 100


#2 print even and odd numbers
# for i in range(2 , 11 , 2):
#     print(i)

# output:
# 2
# 4
# 6
# 8
# 10

# for i in range(1,10,2):
#     print(i)

# output:
# 1
# 3
# 5
# 7
# 9


#3 Factorial of number
# num = 5
# fact = 1
# for i in range(1,num+1):
#     fact = fact * 1
# print("Factorial:" , fact)

# output:
# Factorial: 1


#4 Prime number check
# num = 7
# count = 0
# for i in range(1,num+1):
#     if num % i == 0:
#         count = count + 1

# if count == 2:
#     print("Prime number")
# else:
#     print("Not prime")

# output:
# Prime number