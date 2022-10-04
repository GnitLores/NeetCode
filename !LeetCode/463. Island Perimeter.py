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

    # Breadth first search solution.
    # Find the first island tile and start a BFS from it.
    # Check every direction, and if it is outside the array or
    # not an island tile, add a border.
    # If it is an unvisited island tile, add it to the queue.
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def findStartPoint():
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        return r, c
        r, c = findStartPoint()

        queue = deque()
        visited = set()
        queue.append((r, c))
        visited.add((r, c))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        res = 0
        while queue:
            pr, pc = queue.popleft()

            for dr, dc in dirs:
                r = pr + dr
                c = pc + dc
                if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                    res += 1
                else:
                    if not (r, c) in visited:
                        queue.append((r, c))
                        visited.add((r, c))
        return res

sol = Solution()
print(sol.islandPerimeterSimple(grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]))
print(sol.islandPerimeterSimple(grid = [[1]]))
print(sol.islandPerimeterSimple(grid = [[1,0]]))
print("")
print(sol.islandPerimeter(grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]))
print(sol.islandPerimeter(grid = [[1]]))
print(sol.islandPerimeter(grid = [[1,0]]))