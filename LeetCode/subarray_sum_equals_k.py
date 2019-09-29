# 560: Subarray Sum Equals K 

# Given an array of integers and an integer k, you need to find the 
# total number of continuous subarrays whose sum equals to k.

class Solution:
    def subarraySum(self, nums, target):
        sums = {0: 1}  # prefix sum array
        count = sum = 0
        for n in nums:
            sum += n  # increment current sum
            # check if there is a prefix subarray we can take out to reach k
            count += sums.get(sum - target, 0)
            sums[sum] = sums.get(sum, 0) + 1  # add current sum to sum count
        return count
