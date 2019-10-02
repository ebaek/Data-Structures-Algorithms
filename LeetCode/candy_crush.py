# 723. Candy Crush

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        while True:
            crush = set()

            # find candy matches
            for height in range(len(board)):
                for row in range(len(board[0])):
                    if height > 1 and board[height][row] and board[height][row] == board[height-1][row] == board[height-2][row]:
                        crush |= {(height, row), (height-1, row),
                                  (height-2, row)}

                    if row > 1 and board[height][row] and board[height][row] == board[height][row-1] == board[height][row-2]:
                        crush |= {(height, row), (height, row-1),
                                  (height, row-2)}

            # break out of the loop if there are no matches
            if not crush:
                break

            # set the candy to 0 if there are matches
            for height, row in crush:
                board[height][row] = 0

            # crush the candy
            for row in range(len(board[0])):
                idx = len(board) - 1
                for height in reversed(range(len(board))):
                    if board[height][row] != 0:
                        board[idx][row] = board[height][row]
                        idx -= 1

                for height in range(idx+1):
                    board[height][row] = 0

        return board
