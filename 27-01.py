# 4 Write a program to check if a number is an Armstrong number.
# num = int(input("Enter the number : "))

# temp = num
# sum = 0
# while temp > 0:
#     digit  = temp %10
#     cube = digit ** 3
#     sum = sum + cube      
#     temp //= 10 

# if sum == num:
#     print("It is an armstong number ")
# else:
#     print("Not an armtrong number")

# 5 Write a program to generate the Fibonacci series up to a given number.

# a = 0
# b = 1

# num = int(input("Enter the number : "))

# if num == 1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(1,num+1):
#      c= a+b
#      a= b
#      b = c
#      print(c)

# 6  Write a program to check if a string is a palindrome or not.
# num = (input("Enter the string : "))
# rev = num[::-1]

# if num == rev:
#     print("It is a palindrome")
# else:
#     print("Not a palindrome")

# 7 Write a program to create different star patterns (e.g., pyramid, diamond
#     *
#    ***
#   *****
#  *******
# *********

# num = int(input("Enter the number"))

# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end ="")
#     for j in range(2*i+1):
#         print("*",end = "")
#     print()

# 8 Write a program to compute the factorial of a given number.

# num = int(input("Enter the number : "))

# fact = 1
# while num >0:
#     fact = fact*num
#     num = num - 1
# print("Factorial", fact)

# 9 Write a program to calculate the sum of digits of a number.

# num = int(input("Enter the number : "))
# sum = 0

# while num>0:
#     sum = sum + num % 10
#     num //=10
# print(sum)

# 10  Write a program to find the GCD of two numbers.
# def gcd(x,y):
#     if x>y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1,smaller+1):
#         if ((x % i == 0) and (y % i == 0)):
#             hcf = i
#     return hcf
# print("The HCF of two given numbers is : ",gcd(15,30))

