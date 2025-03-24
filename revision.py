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
#     print(length)
#     while(left<right):
#         if n[left] != n[right]:
#             return False
#         left+=1
#         right-=1
#     return True
# string = input("Enter the string : ")
# if palidrome(string):
#     print(f"{string} is a  palindrome")
# else:
#     print(f"{string} is not a  palindrome")

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

# def rev(n):
#     reversed_str= ""
#     for char in n:
#         reversed_str =  char + reversed_str
#     return reversed_str

# str = input("Enter the string : ")
# print(f" reversed string is {rev(str)}")

# 10 Write a program to find the largest and smallest numbers in an array

# def find_largest_smallest(arr):
#     if not arr:
#         return None
    
#     smallest = largest = arr[0]

#     for num in arr:
#         if num < smallest:
#             smallest = num
#         if num > largest:
#             largest = num
            
#     return smallest, largest

# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# if numbers:
#     smallest, largest = find_largest_smallest(numbers)
#     print(f"Smallest: {smallest}, Largest: {largest}")
# else:
#     print("Error:No number was entered.")

# 11 Write a program to find the sum of elements in an array

# def array_sum(arr):
#     total = 0
#     for num in arr:
#         total+=num
#     return total

# arr = list(map(int,(input("Enter the array :").split())))
# result = array_sum(arr)
# print("Sum of elements : ", result)

# 12 Write a program to find the GCD of two numbers
# def gcd(num1,num2):
#     while num2:
#         num1,num2 = num2 , num1 % num2
#     return num1

# num1,num2  = map(int,(input("Enter two numbers :").split()))
# result = gcd(num1,num2)
# print(f"GCD of {num1} and {num2} is {result}")

# 13 Write a program to generate multiplication tables for a given number.

# def table(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")


# table(5)
# 14 Write a program to find the sum of all even numbers within a given range
# def sum_of_even(start,end):
#     total = 0
#     for i in range(start,end+1):
#         if i % 2 ==0:
#             total +=i
#     return total

# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# result = sum_of_even(start,end)
# print(f"Sum of even numbers between {start} and {end} = {result}")

# 15 Write a program to find the sum of all odd numbers within a given range
# def sum_of_odd(start,end):
#     total = 0
#     for i in range(start,end+1):
#         if i % 2 !=0:
#             total +=i
#     return total

# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# result = sum_of_odd(start,end)
# print(f"Sum of odd numbers between {start} and {end} = {result}")

# 16 Write a program to find all prime numbers within a given range
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# print("Prime numbers:", [num for num in range(start, end + 1) if is_prime(num)])


# 17 Write a program to determine if a number is a perfect number

# def is_perfect(n):
#     sum_of_divisors = 0
#     if n<=1:
#         return False
    
#     for i in range(1,n):
#         if n % i == 0:
#             sum_of_divisors +=i
#     return sum_of_divisors == n

# num = int(input("Enter the number : "))
# if is_perfect(num):
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} is not a perfect number")

# 18 Write a program to find the sum of all even numbers within a given range

# def sum_of_num(n):
#     total = 0
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             total +=i
#     return total

# num = int(input("Enter the number : "))
# result = sum_of_num(num)
# print(f"The sum of even number are in range of 1 to {num}  = {result}")

# 19 Write a program to find the sum of all odd numbers within a given range

# def sum_of_num(n):
#     total = 0
#     for i in range(1,n+1):
#         if i % 2 != 0:
#             total +=i
#     return total

# num = int(input("Enter the number : "))
# result = sum_of_num(num)
# print(f"The sum of even number are in range of 1 to {num}  = {result}")

# 20 Write a program to print all prime numbers less than a given number

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def is_less_prime(limit):
    for num in range(2,limit):
        if is_prime(num):
            print(num,end = " ")

n = int(input("Enter the limit : "))
print(f"Prime number less than {n}")
is_less_prime(n)

