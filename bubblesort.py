def printSortedArray(arr):
    for element in arr:
        print(element,end=" ")

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            printSortedArray(arr)
            print()
    

print("Enter elements of the array: ")
numlist=list(map(int,input().split()))
print("Before sorting:")
printSortedArray(numlist)
print()
print("After sorting:")
bubbleSort(numlist)
printSortedArray(numlist)

