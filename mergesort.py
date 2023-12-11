#merge sort algorithm is based on divide and conquer strategy
#the array is divided into subarrays until all the subarrays contain a single element
#then all these subarrays are again combined in such a way that
#the elements in the subarrays are in sorted manner
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2

    l_half=arr[:mid]
    r_half=arr[mid:]
    l_half=mergeSort(l_half)
    r_half=mergeSort(r_half)
    return merge(l_half,r_half)

def merge(left,right):
    new=[]
    i,j=0,0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    
    new.extend(left[i:])
    new.extend(right[j:])

    return new




nums=[10,9,8,7,6,5,4,3,2,1]
print(mergeSort(nums))
