# 322. Coin Change
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf') for _ in range(amount)]
        
        for i in range(amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        if dp[-1] == float('inf'): return -1
        
        return dp[-1]
        

coins = [1,2,5]
amount = 5
a = Solution()
change = a.coinChange(coins, amount)
print(change)
        
        
