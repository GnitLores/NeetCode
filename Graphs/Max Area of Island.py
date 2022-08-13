from typing import List
import collections

# Breadth first search solution very similar to the Number of Islands problem.
# For each island, calculate the area and record max island area.
# O(rows*columns) time and space complexity.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxArea = [0]
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r, c):
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))
            islandArea = 1

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(rows) and c in range(cols):
                        if (r, c) not in visited and grid[r][c] == 1:
                            queue.append((r, c))
                            visited.add((r,c))
                            islandArea += 1
            maxArea[0] = max(maxArea[0], islandArea)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    bfs(r, c)
        return maxArea[0]

sol = Solution()
grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(sol.maxAreaOfIsland(grid))