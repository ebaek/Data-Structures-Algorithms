# 200: Number of Islands 


class Solution(object):
    def numIslands(self, grid: List[List[str]]) -> int:
        try:
            height, width = len(grid), len(grid[0])
        except:
            return 0

        def dfs(i, j, board):
            board[i][j] = 0  # Mark as 0 to indicate visited status
            for currentX, currentY in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= currentX < len(board) and 0 <= currentY < len(board[0]) and board[currentX][currentY] == "1":
                    dfs(currentX, currentY, board)
            return

        count = 0
        for currentX in range(height):
            for currentY in range(width):
                if grid[currentX][currentY] == "1":
                    dfs(currentX, currentY, grid)
                    count += 1
        return count
