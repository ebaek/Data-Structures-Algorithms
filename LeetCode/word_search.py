# 79: Word Search
# Approach:
# dfs approach: keep track of col, row, lettersSoFar, and nextLetter (index of word)
# check if x, y coordinates are within the bounds -> add coordinate to visited set
# base case is if the lettersSoFar == word, then return True 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width, height = len(board[0]), len(board)
        firstLetter, visited = word[0], set()
        
        def dfs(col, row, lettersSoFar, nextLetter):
            if lettersSoFar == word: return True
            else:
                for moveY, moveX in ((col,row+1), (col+1,row), (col-1,row), (col, row-1)):
                    if lettersSoFar == word[0:nextLetter]:
                        if 0 <= moveY < height and 0 <= moveX < width and (moveY, moveX) not in visited:
                            visited.add((moveY, moveX))
                            if dfs(moveY, moveX, lettersSoFar + board[moveY][moveX], nextLetter+1): 
                                return True
                            else:
                                visited.remove((moveY, moveX))
            return False 

        for col in range(height):
            for row in range(width):
                if board[col][row] == firstLetter:
                    visited.add((col, row))
                    if dfs(col, row, board[col][row], 1): 
                        return True
                    else:
                        visited.remove((col, row))
        
        return False 