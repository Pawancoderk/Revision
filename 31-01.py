# 11 Write a program to find the LCM of two numbers.
# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))

# max_value = max(a,b)

# while(True):
#     if(max_value % a == 0 and max_value % b == 0):
#         break
#     else:
#         max_value = max_value +1

# print(f"The LCM of {a} and {b} is : {max_value}")

# 12Write a program to count vowels and consonants in a given string.

# a = input("Enter the string : ")

# vowel = 0
# consonants = 0

# for i in range(0,len(a)):
#     if (a[i]!= " "):
#         if (a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u" or  
#             a[i] == "A" or a[i] == "E" or a[i] == "I" or a[i] == "O" or a[i] == "U"):
#             vowel = vowel +1
#         else:
#             consonants = consonants +1

# print(f"Total no of vovels : {vowel}")
# print(f"Total no of consonants : {consonants}")

# 13Write a program to reverse a given string.
# a = input("Enter the string : ")

# # print(a[-1::-1])
# for i in range((len(a)-1),-1,-1):
#     print(a[i],end = "")

# 14  Write a program to find the largest and smallest numbers in an array

# a = []
# size = int(input("Enter the size of list"))
# for i in range(size):
#     num = int(input("Enter the number"))
#     a.append(num)
# max = a[0]
# for i in range(size):
#     if a[i] > max:
#         max = a[i]

# print (f"Max number is : {max}")


