# QuickSort 
# Divide and Conquer Algorithm Like Merge Sort
# Picks element as pivot and partitions array around the picked pivot

# partition() takes pivot position and array.
# goal is to put element at correction position in sorted array
# and put all smaller elements before element and all greater elements after 

# Time Complexity: O(nlog(n))


def partition(arr, low, high):
    i = low - 1
    partition = arr[high]

    for j in range(low, high):
        if arr[j] < arr[high]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)

        quicksortLeft = quicksort(arr, low, pivot-1)
        quicksortRight = quicksort(arr, pivot+1, high)

arr = [4, 3, 5, 1, -2, 1]
quicksorted = quicksort(arr, 0, len(arr)-1)
print(arr)


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
