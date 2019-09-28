# MERGE SORT 
# Divide and Conquer Algorithm that keeps splitting list of elements in half until only 1 element remains in the array
    # Adjacent elements become sorted pairs and then sorted pairs are merged with other sorted pairs

# Important:
# Merge sort returns a new array rather than mutating the original array

# Time Complexity:
# O(nlog(n)) - merge sort function splits given array into two and recursively sorts the subarrays
    # because input is being halved and is recursively sorted

# Applications:
# Useful for sorting LinkedLists in O(nlog(n)) time because inserting items in the midpoint 
# takes O(1) space and O(1) time => merge operation of merge sort can be implemented without extra space for linked lists.
# Better than QuickSort because QuickSort requires random access to the ith index 

# Notes:
#  Arrays: elements are contiguous in memory 

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # midpoint
        L, R = arr[:mid], arr[mid:]

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        leftIdx = rightIdx = currentPointer = 0

        # Copy data to temp arrays L[] and R[]
        while leftIdx < len(L) and rightIdx < len(R):
            if L[leftIdx] < R[rightIdx]:
                arr[currentPointer] = L[leftIdx]
                leftIdx += 1
            else:
                arr[currentPointer] = R[rightIdx]
                rightIdx += 1
            currentPointer += 1

        # Checking if any element was left
        while leftIdx < len(L):
            arr[currentPointer] = L[leftIdx]
            leftIdx += 1
            currentPointer += 1

        while rightIdx < len(R):
            arr[currentPointer] = R[rightIdx]
            rightIdx += 1
            currentPointer += 1