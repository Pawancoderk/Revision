# 21 Write a program to find the sum of all even numbers within a given range.

# sum_all = 0
# n = int(input("Enter the number : "))
# for i in range(1,n):
#     if i%2 ==0:
#         sum_all +=i    
# print(sum_all)

# 22  Write a program to find the sum of all odd numbers within a given range

# sum_all = 0
# n = int(input("Enter the number : "))
# for i in range(1,n):
#     if i%2 !=0:
#         sum_all +=i    
# print(sum_all)

# 23 Write a program to find the Fibonacci number at a specific position.

# 24  Write a program to count the number of digits in a given number.
# n= (1,2,3,4,5)
# print(len(n))

# 25 Write a program to print all prime numbers less than a given number


# def print_primes_below(n: int):
#     for num in range(2, n):
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=" ")
#     print()

# # User input
# number = int(input("Enter a number: "))
# print_primes_below(number)

# 27 Write a program to generate number patterns

# 1  
# 2 3  
# 4 5 6  

# n = int(input("Enter the number"))
# num = 1
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(num,end = " ")
#         num  = num +1
#     print()