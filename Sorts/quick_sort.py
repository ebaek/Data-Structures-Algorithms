# QuickSort 
# Divide and Conquer Algorithm Like Merge Sort
# Picks element as pivot and partitions array around the picked pivot

# partition() takes pivot position and array.
# goal is to put element at correction position in sorted array
# and put all smaller elements before element and all greater elements after 

# Time Complexity: O(nlog(n))

import random
# in place
def quick_sort(list, first, last):
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
            
    quick_sort(list, first, right)
    quick_sort(list, left, last)


def quick_sort(list):
    if len(list) < 2:
        return list

    pivot = list.pop()
    left = filter(lambda x: x <= pivot, list)
    right = filter(lambda x: x > pivot, list)

    return quick_sort(left) + [pivot] + quick_sort(right)
