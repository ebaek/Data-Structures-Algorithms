# 213: House Robber II

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))
        
    def rob_helper(self, nums):
        if len(nums) == 0: return 0
        
        dp = [0 for _ in range(len(nums)+1)]        
        dp[1] = nums[0]
        
        for numIdx in range(2, len(nums)+1):
            dp[numIdx] = max(dp[numIdx-1], nums[numIdx-1]+dp[numIdx-2])
        
        return dp[-1]