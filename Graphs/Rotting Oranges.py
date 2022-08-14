from typing import List
import collections

# 0: empty cell,
# 1: fresh orange
# 2: rotten orange.
# Solution using BFS.
# We can't just complete search for one orange at a time.
# Instead we add all freshly rotted oranges to queue and do one round of BFS at a time.
# Count the number of rounds it takes to rot all oranges.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = set()

        justRotted = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    justRotted.append((r, c))
                if grid[r][c] == 1:
                    fresh.add((r, c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0
        while justRotted:
            freshFound = False
            for _ in range(len(justRotted)): # Do one round for all freshly rotted oranges
                coords = justRotted.popleft()
                for dr, dc in directions:
                    r = coords[0] + dr
                    c = coords[1] + dc

                    if r in range(rows) and c in range(cols):
                        if grid[r][c] == 1:
                            freshFound = True
                            justRotted.append((r, c))
                            grid[r][c] = 2
                            fresh.remove((r, c))
            if freshFound:
                time += 1

        if fresh:
            time = -1

        return time

sol = Solution()
oranges = [[2,1,1],[1,1,0],[0,1,1]]
print(sol.orangesRotting(oranges))