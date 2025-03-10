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
def fibo(limit):
    a,b = 0,1
    ans = []
    while (a<=limit):
        ans.append(a)
        a,b = b , a+b
    return ans

num = int(input("Enter input number : "))
print(f"Fibonacci series  :{fibo(num)}")








