# QuickSort 
# Divide and Conquer Algorithm Like Merge Sort
# Picks element as pivot and partitions array around the picked pivot

# partition() takes pivot position and array.
# goal is to put element at correction position in sorted array
# and put all smaller elements before element and all greater elements after 

# Time Complexity: O(nlog(n))

import random
# in place
def quicksort(list, first, last):
    if first >= last: return

    left, right = first, last
    pivot = random.int(left, right)

    while left <= right:
        while list[left] < pivot:
            left += 1
        while list[right] > pivot:
            right -= 1
        if left <= right:
            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1
            
    quicksort(list, first, right)
    quicksort(list, left, last)


def quicksort_inplace(arr, low=0, high=None):
    def partition(arr, low, high):
        pivotPointer = low-1
        pivot = arr[high]

        for currentPos in range(low, high):
            if arr[currentPos] <= pivot:
                pivotPointer += 1
                arr[pivotPointer], arr[currentPos] = arr[currentPos], arr[pivotPointer]

        arr[pivotPointer+1], arr[high] = arr[high], arr[pivotPointer+1]
        return pivotPointer+1

    if high == None: high = len(arr)-1
    if low < high:
        partitionIdx = partition(arr, low, high)
        quicksort_inplace(arr, low, partitionIdx-1) # sort lower half
        quicksort_inplace(arr, partitionIdx+1, high) # sort upper half 
    

# space inefficient algo
def quicksort(list):
    if len(list) < 2:
        return list

    pivot = list.pop()
    left = filter(lambda x: x <= pivot, list)
    right = filter(lambda x: x > pivot, list)

    return quicksort(left) + [pivot] + quicksort(right)


arr = [3,5,2,1,6]
a = quicksort_inplace(arr)
print(arr)
