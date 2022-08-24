class Solution:
    # Dynamic programming solution.
    # Since we can only move down and right, the number of ways to reach a tile is the number
    # of ways to reach the tile above plus the number of ways to reach the tile to the left.
    # Every tile in the top row and in the left column can only be reached in one way.
    # From this we can calculate every other tile.
    # O(n*m) time and space.
    def uniquePaths(self, m: int, n: int) -> int:
        board = [None] * m
        for r in range(m):
            board[r] = [1] * n if r == 0 else [1] * n
            board[r][0] = 1

        for r in range(1, m):
            for c in range(1, n):
                board[r][c] = board[r - 1][c] + board[r][c - 1]
        
        return board[-1][-1]

sol = Solution()
print(sol.uniquePaths(3, 7))
print(sol.uniquePaths(3, 2))