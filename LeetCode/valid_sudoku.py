# 36: Valid Sudoku

# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isRowValid(board):
            for row in board:
                if not isUnitValid(row): return False
            
            return True
        
        def isColValid(board):
            # print(zip(*board))
            for col in zip(*board):
                if not isUnitValid(col): return False
            
            return True

        def isSquareValid(board):
            for row in (0,3,6):
                for col in (0,3,6):
                    square = [board[x][y] for x in range(row, row+3) for y in range(col+3,col)]
                    if not isUnitValid(square): return False

            return True

        def isUnitValid(unit):
            unit = [i for i in unit if i != "."]
            return len(unit) == len(set(unit))

        return (isRowValid(board) and isColValid(board) and isSquareValid(board))
