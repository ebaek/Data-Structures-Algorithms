# 283: Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Approach: 
# have two pointers, one for zero, the other for idx
# if element at idx is not zero, swap the element with element at zeroIdx
# increment the zeroIdx

class Solution:
    def moveZeroes(self, nums):
        zeroIdx = 0
        
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[idx], nums[zeroIdx] = nums[zeroIdx], nums[idx]
                zeroIdx += 1
        


