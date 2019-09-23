# 698. Partition to K Equal Sum Subsets
# Given an array of integers nums and a positive integer k, 
# find whether it's possible to divide this array into k non-empty 
# subsets whose sums are all equal.
 
# Example 1:
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets:
# (5), (1, 4), (2,3), (2,3) with equal sums.

# Approach
# fill k buckets with booleans, True = sum at that bucket meets target
# recursively call to check if other buckets will meet target, if not set bucket back to False 
# and try adding the next element in the array


class Solution(object):
    def canPartitionKSubsets(self, nums, k):

        def dfs(curSum, k, startIdx):
            if k == 1: return True

            if curSum == target:
                return dfs(nums, 0, k-1, 0)

            for idx in range(startIdx, len(nums)):
                if buckets[idx] == False:
                    buckets[idx] = True
                    
                    if dfs(curSum+nums[idx], k, idx+1): return True
                    buckets[idx] = False

            return False

        total = sum(nums)

        if k == 0 or total % k != 0: return False
        target = total//k

        buckets = len(nums) * [False]
        return dfs(0, k, 0)


