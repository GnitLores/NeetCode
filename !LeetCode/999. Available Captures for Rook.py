from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def findRook():
            for r in range(8):
                for c in range(8):
                    if board[r][c] == "R":
                        return r, c

        def findCapture(arr):
            for n in arr:
                if n == "p":
                    return 1
                elif n == "B":
                    return 0
            return 0

        r, c = findRook()
        row = board[r]
        col = [i[c] for i in board]

        res = 0
        res += findCapture(row[:c + 1][::-1]) # Reverse to go left
        res += findCapture(row[c:]) # Go right
        res += findCapture(col[:r + 1][::-1]) # Reverse to go up
        res += findCapture(col[r:]) # Go down
            
        return res

sol = Solution()
print(sol.numRookCaptures(board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
print(sol.numRookCaptures(board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
print(sol.numRookCaptures(board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))