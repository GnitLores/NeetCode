from typing import List


class Solution:
    # Backtracking solution.
    # For each row, place a queen in a column and continue the DFS for the next row.
    # Track blocked possitions with sets.
    # Rows are automatically handled as we only place one queen per row at a time.
    # Columns are indicated by column index.
    # Positive (upward sloping) diagonals are indicated by row + col which is constant.
    # Negative diagonals are indicated by row - col which is also constant.
    # Positive example: 3 + 0 = 2 + 1 = 1 + 2 = 0 + 3 = 3
    # Negative example: 1 - 0 = 2 - 1 = 3 - 2 = 1
    # This way, all lanes can be check in O(1) time.
    # Otherwise this is a brute force backtracking solution.
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1: return [['Q']]
        queens = set()
        cols = set()
        posDiags = set()
        negDiags = set()

        validPositions = []
        def dfs(r):
            if len(queens) == n:
                validPositions.append(queens.copy())

            for c in range(n):
                if c in cols or (r + c) in posDiags or (r - c) in negDiags:
                    continue

                queens.add((r, c))
                cols.add(c)
                posDiags.add(r + c)
                negDiags.add(r - c)
                dfs(r + 1)
                queens.remove((r, c))
                cols.remove(c)
                posDiags.remove(r + c)
                negDiags.remove(r - c)

        dfs(0)

        res = []
        for coords in validPositions:
            board = [['.' for _ in range(n)] for _ in range(n)]
            for r, c in coords:
                board[r][c] = 'Q'
                board[r] = "".join(board[r])
            res.append(board)
        return res

def printBoards(boards):
    print("")
    for b in range(len(boards)):
        print("Board " + str(b + 1))
        for r in range(len(boards[b])):
            print(boards[b][r])

sol = Solution()
printBoards(sol.solveNQueens(4))
printBoards(sol.solveNQueens(5))
