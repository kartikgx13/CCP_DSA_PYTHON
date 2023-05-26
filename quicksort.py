#quick sort is based on divide and conquer algorithm
#it is based on recursion
#the whole array is divided into subarrays about the pivot point
#these subarrays are then sorted using the same process
#until each subarray consists of a single element
#then all these elements are combined to give the sorted array
def printsortedArray(arr):
    for element in arr:
        print(element,end=" ")

def partition(arr,low,high):

    #in our case we will set the rightmost element as pivot hence:
    pivot=arr[high]

    #in quick sort we always have two pointers i and j i will be -1 and j will start from 0th positon so that they both can be swapped later on
    i=low-1

    #now we will traverse through all elements
    #we will compare each element with the pivot
    for j in range(low,high):
        if arr[j]<=pivot:
            i += 1           #if element found is less than pivot we will increment i and swap i and j respectively
            arr[i],arr[j]=arr[j],arr[i]

    #after doing this now we need to change the positon of pivot
    #so we swap it with greater element pointed by i+1
    arr[i+1],arr[high]=arr[high],arr[i+1]

    return i+1 #here we returned the position from where the partition was done

def quickSort(arr,low,high):
    if low<high: 
        #by doing this elements to the left of pivot are smaller than it
        #and elements to the right are greater than it


        pi=partition(arr,low,high)

        quickSort(arr,low,pi-1)  #calling the function recursively for left and right subarrays

        quickSort(arr,pi+1,high)
        
print("Enter elements of the array:")
numlist=list(map(int,input().split()))
print("Before sorting:")
print()
printsortedArray(numlist)
print("After sorting:")
size=len(numlist)
quickSort(numlist,0,size-1)
printsortedArray(numlist)