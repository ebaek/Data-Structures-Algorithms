# 53: Maximum Subarray

# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum 
# and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding 
# another solution using the divide and conquer approach, which is more subtle.

# Input: [-2,1,-3,4,-1,2,1,-5,4],

# Time Complexity: O(n)
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        maxEndingHere, maxSoFar = float('-inf'), float('-inf')

        for num in nums:
            maxEndingHere = max(maxEndingHere + num, num)
            maxSoFar = max(maxSoFar, maxEndingHere)

        return maxSoFar
            

        
