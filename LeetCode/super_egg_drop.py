# 887: Super Egg Drop

class Solution:
    # brute force solution 
    # time complexity: O(eggs*floors^2)
    # space complexity: O(eggs * floors)
    # doesn't work with leet 
    def superEggDrop(self, eggs: int, floors: int) -> int:        
        dp = [[float('inf')]*(floors+1) for _ in range(eggs+1)]
        
        # if 0 floors, 0 drops. if 1 floor, 1 drop.
        for i in range(1, eggs+1):
            dp[i][0] = 0
            dp[i][1] = 1
            
        # if 1 egg, worst possible number of drops is number of floors
        for currFloor in range(1, floors+1):
            dp[1][currFloor] = currFloor
        
        for egg in range(2, eggs+1):
            for floor in range(2, floors+1):
                for floorAttempt in range(1, floor+1):
                    dp[egg][floor] = min(dp[egg][floor], 1 + max(dp[egg-1][floorAttempt-1], dp[egg][floor-floorAttempt]))
        return dp[eggs][floors]
    

class Solution(object):
    def superEggDrop(self, eggs, floors):
        #initialize graph
        dp = [[float('inf')]*(floors+1) for _ in range(eggs+1)]

        # if 0 floors, 0 attempts, if 1 floor, 1 attempt
        for egg in range(1, eggs+1):
            dp[egg][0] = 0
            dp[egg][1] = 1

        # if egg is 1 max
        for floor in range(1, floors+1):
            dp[1][floor] = floor

        for egg in range(2, eggs+1):
            currFloorAttempt = 1
            for floor in range(2, floors+1):
                while currFloorAttempt < floors+1 and dp[egg][floor-currFloorAttempt] > dp[egg-1][currFloorAttempt-1]:
                    currFloorAttempt += 1
                dp[egg][floor] = 1 + dp[egg-1][currFloorAttempt-1]

        return dp[eggs][floors]

a = Solution()
b = a.superEggDrop(3,4)
print(b)
        


