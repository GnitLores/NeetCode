from typing import List


class Solution:
    # - If a square has zero cubes, it contributes nothing to the surface area.
    # - If a square has at least one cube, it contributes at least 2 to the surface area from the top and bottom.
    # The surface area to the left, right, above, and below are found in the following way:
    # - If the square is at the edge in that direction, all cubes contribute in that direction.
    # - If not at the edge, only the cubes above the cubes on the adjacent square contribute in that direction.
    def surfaceArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                n = grid[r][c]
                if n == 0: continue
                res += 2 # Top / bottom
                res += n if r == 0          else max(0, n - grid[r - 1][c]) # Left
                res += n if r == rows - 1   else max(0, n - grid[r + 1][c]) # Right
                res += n if c == 0          else max(0, n - grid[r][c - 1]) # Above
                res += n if c == cols - 1   else max(0, n - grid[r][c + 1]) # Below
        return res

sol = Solution()
print(sol.surfaceArea(grid = [[1,2],[3,4]]))
print(sol.surfaceArea(grid = [[1,1,1],[1,0,1],[1,1,1]]))
print(sol.surfaceArea(grid = [[2,2,2],[2,1,2],[2,2,2]]))