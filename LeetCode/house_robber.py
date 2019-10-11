# 198: House Robber 

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        dp = [0 for _ in range(len(nums))] 
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for idx in range(2, len(nums)):
            dp[idx] = max(nums[idx] + dp[idx-2], dp[idx-1])
        
        return dp[-1]
        
        