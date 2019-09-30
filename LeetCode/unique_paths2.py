# 63: Unique Paths 2

# DP table 

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height, width = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[0]*width for _ in range(height)]
        if obstacleGrid[0][0] == 1:
            return 0

        for y in range(height):
            for x in range(width):
                grid[y][x] = 0

        grid[0][0] = 1
        for y in range(0, height):
            for x in range(0, width):
                if obstacleGrid[y][x] == 1:
                    continue
                if y > 0:
                    grid[y][x] += grid[y-1][x]
                if x > 0:
                    grid[y][x] += grid[y][x-1]

        return grid[height-1][width-1]
