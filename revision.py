# 1 Write a program to check whether a number is even or odd.
# def odd_even(n):
#     if (n // 2)*2 == n:
#         print("The number is even")
#     else:
#         print("The number is  odd")


# odd_even(8)

# 2  Write a program to determine if a number is prime.

# def prime(n):
#     if n< 2:
#         return False
#     for i in range(2 , int(n**0.5)+1):
#         if n % i == 0 :
#             return False
#     return True

# num = int(input("Enter the number : "))
# if prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# 3 Write a program to check if a number is an Armstrong number.
# def arm(n):
#     num = n
#     sum = 0
#     length = len(str(num))

#     while num >0:
#         digit = num % 10
#         sum += digit ** length
#         num//=10
      
#     return sum == n

# nums = int(input("Enter the number : "))
# if arm(nums):
#     print(f"{nums} is a armstrong number")
# else:
#     print(f"{nums} is not a armstrong number")

# 4 Write a program to generate the Fibonacci series up to a given number.
# def fibo(limit):
#     a,b = 0,1
#     ans = []
#     while (a<=limit):
#         ans.append(a)
#         a,b = b , a+b
#     return ans

# num = int(input("Enter input number : "))
# print(f"Fibonacci series  :{fibo(num)}")

# 5  Write a program to check if a string or number is a palindrome.

# def palidrome(n):
#     length = len(n)
#     left = 0
#     right = length -1 
#     while(left<right):
#         if n[left] != n[right]:
#             return False
#         left+=1
#         right-=1
#     return True
# string = input("Enter the string : ")
# if palidrome(string):
#     print(f"{string} is palindrome")
# else:
#     print(f"{string} is not palindrome")

# 6 Write a program to create different star patterns (e.g., pyramid, diamond)

#     *
#    ***
#   *****
#  *******
# *********

# def pattern(n):
#     for i in range(1,n+1):
#         print(" "*(n-i),"*"*(2*i-1))

# num = int(input("Enter the digit : "))
# pattern(num)

# 7 Write a program to compute the factorial of a given number
# def fac(n):
#     if n<0 :
#         return "Factorial id not defined for negative number"
#     result = 1
#     for i in range(1,n+1):
#         result*=i  # result = result * i
#     return result

# num = int(input("Enter the number : "))
# print(f"factorial of {num} is {fac(num)}")

# 8 Write a program to calculate the sum of digits of a number.
# def sum_of(n):
#     sums = 0
#     while n>0 :
#         digit = n % 10
#         sums +=digit
#         n //=10
#     return sums

# num = int(input("Enter the number : "))
# result = sum_of(num)
# print(f"Sum of digits:",result)

# 9 Write a program to reverse a given string.

def rev(n):
    reversed_str= ""
    for char in n:
        reversed_str =  char + reversed_str
    return reversed_str

str = input("Enter the string : ")
print(f" reversed string is {rev(str)}")

# 10 Write a program to find the largest and smallest numbers in an array











    










