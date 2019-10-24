# 525: Contiguous Array

# Given a binary array, find the maximum length of a 
# contiguous subarray with equal number of 0 and 1.

# Approach:
# [0,1,1,0,1,0,1]

# [1, 1, 1, 2, 2, 3, 3]

# [0, 1, 2, 2, 3, 3, 3]

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict = {0:-1}
        maxLength = 0
        count = 0
        
        for idx, num in enumerate(nums):
            if num == 0: count -= 1
            elif num == 1: count += 1
            
            if count in dict: 
                maxLength = max(idx-maxLength[idx], maxLength)
            else:
                dict[count] = idx
        
        return maxLength
        
            
