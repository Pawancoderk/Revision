# 16 Write a program to find the sum of elements in an array
# a = []
# size = int(input("Enter the length of list : "))
# for i in range(size):
#     value = int(input("Enter the value : "))
#     a.append(value)
# sum = 0

# for i in range(size):
#         sum = sum+a[i]
# print(f"The sum is : {sum}")

# 17 Write a program to find all Armstrong numbers within a given range

# lower = int(input("Enter the lower limit: "))
# higher = int(input("Enter the higher limit: "))

# for num in range(lower,higher +1):
#     temp = num
#     sum = 0
#     order = len(str(num))
#     while temp >0:
#         digit = temp %10
#         sum+= digit ** order
#         temp //=10
#     if (num == sum):
#         print(num)

# 18 Write a program to generate multiplication tables for a given number.

# num = int(input("Enter the number"))

# for i in range(1,11):
#      sum = i*num
#      print(f"{num} X {i} = {sum}")

# 19 Write a program to find all prime numbers within a given range

# lower = int(input("Enter the lower range : "))
# higher = int(input("Enter the higher range : "))


# for num in range(lower , higher +1):
#     if num >1:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# 20 Write a program to determine if a number is a perfect number.

# num = int(input("Enter the number"))

# def perfect(num):
#     sum = 0
#     for i in range(1,num):
#         if num %i ==0:
#          sum = sum +i

#     if (num == sum):
#         print("It is a perfect number")
#     else:
#         print("It is not a perfect number")


# perfect(num)

            
        