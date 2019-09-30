# 62: Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.count = 0
        def dfs(currX, currY):
            if currX+1 == m and currY+1 == n: 
                self.count += 1
            else:
                if 0 <= currX + 1< m: 
                    dfs(currX+1, currY)

                if 0 <= currY + 1< n:
                    dfs(currX, currY+1)

        dfs(0,0)
        return self.count
    
# Build a table 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1]*n for _ in range(m)]

        for currX in range(1, m):
            for currY in range(1, n):
                grid[currX][currY] = grid[currX-1][currY] + \
                    grid[currX][currY-1]

        return grid[-1][-1]

        
