# 239: Sliding Window Maximum

# Approach: 
# brute force approach: O(n*) 


class Solution:
    def maxSlidingWindow(self, nums: List[int], window: int) -> List[int]:
        if not nums: return nums
        maxes = []

        def getMaxWindow(sub_arr):
            localMax = float('-inf')
            for num in sub_arr:
                localMax = max(localMax, num)

            return localMax

        idx = 0
        while idx+window <= len(nums):
            localMax = getMaxWindow(nums[idx:idx+window])
            maxes.append(localMax)
            idx += 1

        return maxes
    

from collections import deque
# Optimal solution from LeetCode
class Solution:
    def maxSlidingWindow(self, nums: List[int], window: int) -> List[int]:
        maxes = []
        bigger = deque()
        
        for idx, num in enumerate(nums):
            
            # make sure the rightmost one is the smallest
            while bigger and nums[bigger[-1]] <= num:
                bigger.pop()

            # add in
            bigger.append(idx)

            # make sure the leftmost one is in-bound
            if idx - bigger[0] >= window:
                bigger.popleft()

            # if idx + 1 < window, then we are initializing the bigger array
            if idx + 1 >= window:
                maxes.append(nums[bigger[0]])
                
        return maxes
