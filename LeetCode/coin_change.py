# 322. Coin Change
from typing import List

# tabulation approach 
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

# memoization approach
class Solution:
    def coinChange(self, coins: List[int], amount) -> int:
        memo = {}

        def dfs(amt):
            if amt < 0:
                return -1
            if amt == 0:
                return 0
            if amt in memo:
                return memo[amt]

            for coin in coins:
                numCoins = dfs(amt - coin) + 1
                if not numCoins:
                    continue

                if amt not in memo:
                    memo[amt] = numCoins

                memo[amt] = min(memo[amt], numCoins)

            if amt not in memo:
                memo[amt] = -1

            return memo[amt]

        coins.sort(reverse=True)
        return dfs(amount)


        
        
