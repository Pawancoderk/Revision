# 1 Print name n times using recursion
# def f(i,n):
#     if(i>n):
#         return
#     print("raj")
#     f(i+1,n)


# def main():
#     n = int(input("Enter the number : "))
#     f(1,n)

# main()

# def f(i,n):
#     if(i>n):
#         return
#     print(i)
#     f(i+1,n)


# def main():
#     n = int(input("Enter the number : "))
#     f(1,n)

# main()


# def f(i,n):
#     if(i<1):
#         return
#     print(i)
#     f(i-1,n)


# def main():
#     n = int(input("Enter the number : "))
#     f(n,n)

# main()

# def f(i,n):
#     if(i<1):
#         return
#     f(i-1,n)
#     print(i)


# def main():
#     n = int(input("Enter the number : "))
#     f(n,n)

# main()

# def f(i,n):
#     if(i>n):
#         return
#     f(i+1,n)
#     print(i)


# def main():
#     n = int(input("Enter the number : "))
#     f(1,n)

# main()

# def f(i,sum):
#     if(i<1):
#         return
#     print(sum)
#     f(i-1,sum+1)




# def main():
#     n = int(input("Enter the number: "))
#     f(n,0)


# main()

#Sum of first n natural number
# def f(i,sum):
#     if(i<1):
#         print(sum)
#         return
#     f(i-1,sum+i)

# def main():
#     n = int(input("Enter the number: "))
#     f(n,0)
# main()

# def f(n):
#     if(n == 0):
#         return 0
#     return n + f(n-1)
    


# def main():
#     n = int(input("Enter the number: "))
#     print(f(n))

# main()

#factorial of n natural number using functional recursion
# def f(n):
#     if(n == 0):
#         return 1
#     return n * f(n-1)
    


# def main():
#     n = int(input("Enter the number: "))
#     print(f(n))

# main()

# Reverse ann array using recursion

# arr = [3,47,43,11,9,4,2,1]

# def f(arr,left,right):
#     if(left>=right):
#         return
#     arr[left],arr[right] = arr[right],arr[left]
#     f(arr,left+1,right-1)

# def main():
#     arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
#     left = int(input("Enter the left index: "))
#     right = int(input("Enter the right index: "))
#     f(arr,left,right)
#     print("Reverse",arr)

# main()

## Checking a string is pallindrome or not

# def f(i,s,n):
#     if(i>=n//2):
#         return True
#     if (s[i] != s[n-i-1]):
#         return False
#     return f(i+1,s,n)


# def main():
#     s = input("Enter the string : ")
#     n = len(s)
#     if f(0,s,n):
#         print("Palindrome")
#     else:
#         print("Not a palindrome")

# main()

def f(n):
    if(n<=1):
        return n
    last  = f(n-1)
    slast = f(n-2)
    return last + slast

def main():
    n = int(input("Enter the number : "))
    print(f(n))

main()