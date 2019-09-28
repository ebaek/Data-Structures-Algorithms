#70: Climbing Stairs

# Approach: store the base cases in a memo
# check if n is in the memo, if so return memo[n]
# otherwise, we know that in order to reach n stairs 
# this could be done with a "starting pointer" of decrementing either 1 or 2

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1, 2: 2}
        
        def helper(n):
            if n in memo: return memo[n]
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        
        return helper(n)
