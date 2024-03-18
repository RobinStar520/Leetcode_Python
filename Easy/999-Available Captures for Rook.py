# On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.

# When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

# Return the number of available captures for the white rook.

 

# Example 1:


# Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation: In this example, the rook is attacking all the pawns.
# Example 2:


# Input: board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 0
# Explanation: The bishops are blocking the rook from attacking any of the pawns.
# Example 3:


# Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation: The rook is attacking the pawns at positions b5, d6, and f5.
 

# Constraints:

# board.length == 8
# board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'
# There is exactly one cell with board[i][j] == 'R'

# Approach:
# 1.Find the write rock;
# 2.Check four directions to get how many pawn it can capture.

from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x: int = 0
        y: int = 0
        m: int = len(board)
        n: int = len(board[0])
        result: int = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    x = i
                    y = j
                    break
        for i in range(x, m):
            if board[i][y] == 'B':
                break
            elif board[i][y] == 'p':
                result += 1
                break
        for i in range(x, -1, -1):
            if board[i][y] == 'B':
                break
            elif board[i][y] == 'p':
                result += 1
                break
        for i in range(y, n):
            if board[x][i] == 'B':
                break
            elif board[x][i] == 'p':
                result += 1
                break
        for i in range(y, -1, -1):
            if board[x][i] == 'B':
                break
            elif board[x][i] == 'p':
                result += 1
                break
        return result
