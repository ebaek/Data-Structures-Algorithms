# 518: Coin Change 2 


# Time Complexity: O(amt * num coins)
# Space Complexity: O(amt * num coins)
class Solution:
    def change(self, amt: int, coins: List[int]) -> int:
        if amt == 0: return 1
        if len(coins) == 0: return 0
        
        memo = [[1]+([0]*amt) for _ in range(len(coins))]
        
        for i in range(len(coins)):
            for j in range(1, amt+1):
                memo[i][j] = memo[i - 1][j] + (memo[i][j - coins[i]] if j-coins[i] >= 0 else 0)
        return memo[-1][-1]

# Space optimized
class Solution:
    def change(self, amt: int, coins: List[int]) -> int:
        if amt == 0: return 1
        if len(coins) == 0: return 0
        
        memo = [1] + [0] * amt
        
        for i in range(len(coins)):
            for j in range(1, amt+1):
                memo[j] += memo[j-coins[i]] if j-coins[i] >= 0 else 0
        return memo[-1]
        
    
        
