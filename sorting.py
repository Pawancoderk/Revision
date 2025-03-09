def slection_sort():
    arr = []
    n  = int(input("Enter the size of array: "))
    print("Enter the element in array :")
    for i in range(n):
        arr.append(int(input()))

    for i in range(n-1):
        index = i
        for j in range(i+1,n):
            if (arr[j]<arr[index]):
                index = j
        arr[i],arr[index] = arr[index],arr[i]

    print("Sorted array :",*arr)

# slection_sort()

def bubble_sort(arr,n):
    for i in range(n-1,0,-1):
        swap = 0
        for j in range(i):
            if(arr[j]> arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = 1
        if(swap == 0):
            break
        print("runs")


def main():
    arr = list(map(int,(input("Enter space-separted numbers: ").split())))
    n = len(arr)
    
    print("Original array",arr)
    bubble_sort(arr,n)

    print("Sorted array",arr)

# main() 

def insertion_sort(arr,n):
    for i in range(n-1,0,-1):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j-= 1


def main():
    arr = list(map(int,(input("Enter space-separted : ").split())))
    n = len(arr)
    
    print("Original array",arr)
    insertion_sort(arr,n)

    print("Sorted array",arr)

# main()





























# def bubble_sort(arr, n):  # Function to perform Bubble Sort
#     for i in range(n - 1, 0, -1):  # Loop from n-1 to 1 (not including 0)
#         for j in range(i):  # Loop from 0 to i-1
#             if arr[j] > arr[j + 1]:  # If current element is greater than the next element
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements

# def main():  # Main function
#     n = int(input())  # Take integer input for size of the array
#     arr = [0] * n  # Initialize an array of size n with zeros
    
#     for i in range(n):  # Loop to take input for array elements
#         arr[i] = int(input())
    
#     bubble_sort(arr, n)  # Call bubble_sort function to sort the array
    
#     for i in range(n):  # Loop to print the sorted array
#         print(arr[i])

#     main()

