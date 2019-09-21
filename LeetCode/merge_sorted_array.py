# 88: Merge Sorted Array

# make a duplicate of nums1 approach
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0, 0
        nums1Copy = nums1.copy()

        while i < m or j < n:
            if nums1Copy[i] > nums2[j]:
                nums1[i] = nums2[j]
                j += 1
            else:
                i += 1
        
        if i < n:
            nums1[i+j:] = nums1Copy[i:]
        if j < m:
            nums1[j+j:] = nums2[j:]

# space efficient approach
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1Idx = m - 1
        nums2Idx = n - 1

        mainPointer = m + n - 1

        while nums1Idx >= 0 and nums2Idx >= 0:
            if nums1[nums1Idx] < nums2[nums2Idx]:
                nums1[mainPointer] = nums2[nums2Idx]
                nums2Idx -= 1
            else:
                nums1[mainPointer] = nums1[nums1Idx]
                nums1Idx -=1
            mainPointer -= 1
        
        nums1[:nums2Idx+1] = nums2[:nums2Idx+1]

        
            

