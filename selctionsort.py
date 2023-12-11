def printSortedArray(arr):
    for element in arr:
        print(element,end=" ")

def selectionSort(arr):

    for i in range(len(arr)):
        min_ind=i  #we set this because in selectionsort we consider the first element alreadt sorted hence it becomes the element

        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_ind]:
                min_ind=j             #this will return the index of the lowest element in the unsorted subarray
        #swap the lowest element of the array with our original element
        arr[i],arr[min_ind]=arr[min_ind],arr[i]

print("Enter elements of the array: ")
numlist=list(map(int,input().split()))
print("Before sorting:")
printSortedArray(numlist)
print("After sorting:")
selectionSort(numlist)
printSortedArray(numlist)