# 256: Paint House

# Approach: 
# build the dp table of optimal solutions with the current house
# smallest problem is when there are 0 houses, what are the optimal costs? 0
# next step, only one house (house #0), what are the optimal costs for each option
    # i.e. paint house 0 (red), paint house 1 (green) paint house 2 (blue)
        #  paint house 0 (green), paint house 1 (blue) paint house 2 (red)
        #  paint house 0 (blue), paint house 1 (red) paint house 2 (green)
# keep building until reach optimal solutions if include all houses 
# select the optimal solution of the array of optimal solutions

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        num_colors = 3
        num_houses = len(costs)
        
        dp = [[0]*num_colors for _ in range(num_houses+1)]
        
        for houseIdx in range(1, num_houses+1):
            dp[houseIdx][0] = min(dp[houseIdx-1][1], dp[houseIdx-1][2]) + costs[houseIdx-1][0]
            dp[houseIdx][1] = min(dp[houseIdx-1][0], dp[houseIdx-1][2]) + costs[houseIdx-1][1]
            dp[houseIdx][2] = min(dp[houseIdx-1][0], dp[houseIdx-1][1]) + costs[houseIdx-1][2]
        
        optimal_solutions = dp[-1]
        return min(optimal_solutions)