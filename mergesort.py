#merge sort algorithm is based on divide and conquer strategy
#the array is divided into subarrays until all the subarrays contain a single element
#then all these subarrays are again combined in such a way that
#the elements in the subarrays are in sorted manner
def printSortedArray(arr):
    for element in arr:
        print(element,end=" ")

def mergeSort(arr):
    if len(arr)>1:
        #dividing the array into two subarrays
        mid= len(arr)//2
        L=arr[:mid]       #storing the two subarrays
        M=arr[mid:]

        #calling mergesort recursively
        mergeSort(L)
        mergeSort(M)

        i=j=k=0

        while i<len(L) and j<len(M):    #copying the smallest element out of the two subarrays into the sorted array
            if L[i]<M[j]:
                arr[k]=L[i]
                i += 1
            else:
                arr[k]=M[j]
                j += 1
            
            k += 1
        
        #when we run out of elements in either of the subarray copying the remaining elements

        while i<len(L):
            arr[k]=L[i]
            i += 1
            k += 1
        
        while j<len(M):
            arr[k]=M[j]
            j += 1
            k += 1

print("Enter elements of the array:")
numlist=list(map(int,input().split()))
print("Before sorting:")
printSortedArray(numlist)
print()
print("After sorting:")
mergeSort(numlist)
printSortedArray(numlist)