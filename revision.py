# 1 Write a program to check whether a number is even or odd.
def odd_even(n):
    if (n // 2)*2 == n:
        print("The number is even")
    else:
        print("The number is  odd")


# odd_even(8)

# 2  Write a program to determine if a number is prime.

def prime(n):
    if n< 2:
        return False
    for i in range(2 , int(n**0.5)+1):
        if n % i == 0 :
            return False
    return True

num = int(input("Enter the number : "))
if prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")








