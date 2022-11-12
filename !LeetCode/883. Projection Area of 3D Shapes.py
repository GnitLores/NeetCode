from typing import List


class Solution:
    # The projection on the xy plane does not depend on the number of cubes stacked,
    # if there is at least one cube, it is projected on that square.
    # The xz amd yz projections are the max number of cubes stacked across the rows
    # and columns of the array respectively.
    def projectionArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        xy = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0: xy += 1
        
        xz = 0
        for r in range(rows):
            xz += max(grid[r])
        
        yz = 0
        for c in range(cols):
            colMax = 0
            for r in range(rows):
                colMax = max(colMax, grid[r][c])
            yz += colMax

        return xy + xz + yz

sol = Solution()
print(sol.projectionArea(grid = [[1,2],[3,4]]))
print(sol.projectionArea(grid = [[2]]))
print(sol.projectionArea(grid = [[1,0],[0,2]]))