from collections import deque
from typing import List


class Solution:
    # Simple iterative solution.
    # Go through every tile and if it is an island tile,
    # add a border if it is on the edge of the array
    # or if the adjacent tile in each direction is not an island tile.
    def islandPerimeterSimple(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r == 0 or grid[r - 1][c] == 0: res += 1
                    if r == rows - 1 or grid[r + 1][c] == 0: res += 1
                    if c == 0 or grid[r][c - 1] == 0: res += 1
                    if c == cols - 1 or grid[r][c + 1] == 0: res += 1
        return res

sol = Solution()
print(sol.islandPerimeterSimple(grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]))
print(sol.islandPerimeterSimple(grid = [[1]]))
print(sol.islandPerimeterSimple(grid = [[1,0]]))