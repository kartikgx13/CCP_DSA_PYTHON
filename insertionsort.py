def printSortedArray(arr):
    for element in arr:
        print(element,end=" ")

def insertionSort(arr):
    #loop for passes
    for i in range(1,len(arr)): #here we are starting from 1 because in insertion sort we have to do n-1 passes 
        #loop for each pass
        key=arr[i]
        j=i-1

        while j>=0 and (arr[j]>key):
            arr[j+1]=arr[j]
            j -= 1
        arr[j+1]=key #we did this because at some point j will become -1 but we have to insert the key at 0 hence we did j+1 so that key is inserted at 0th position

print("Enter elements of array: ")
numlist=list(map(int,input().split()))
print("Before sorting:")
printSortedArray(numlist)
print("After sorting:")
print()
insertionSort(numlist)
printSortedArray(numlist)