from typing import List
from collections import deque

class Solution:
    # Breadth first search solution with search done in rounds.
    # A tile located e.g. one up and to the left is the same distance as one located two up.
    # Thus we can first add all tiles touching the center, and then add all tiles touching those tiles
    # and so on.
    # This is in practice a BFS done in rounds.
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        visited = set()
        res = []
        q = deque()
        q.append([rCenter, cCenter])
        visited.add((rCenter, cCenter))

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            for _ in range(len(q)):
                coords = q.popleft()
                res.append(coords)
                r, c = coords
                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    if row >= 0 and row < rows and col >= 0 and col < cols:
                        if (row, col) not in visited:
                            q.append([row, col])
                            visited.add((row, col))
        return res
    
    # Sorting based solution.
    # Generate a list of tuples with coordinates of all tiles and sort the list based on the distance function.
    def allCellsDistOrderSort(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        tiles = [(r, c) for c in range(cols) for r in range(rows)]
        return sorted(tiles, key = lambda p: abs(p[0] - rCenter) + abs(p[1] - cCenter))



sol = Solution()
print(sol.allCellsDistOrder(rows = 1, cols = 2, rCenter = 0, cCenter = 0))
print(sol.allCellsDistOrder(rows = 2, cols = 2, rCenter = 0, cCenter = 1))
print(sol.allCellsDistOrder(rows = 2, cols = 3, rCenter = 1, cCenter = 2))
print("")
print(sol.allCellsDistOrderSort(rows = 1, cols = 2, rCenter = 0, cCenter = 0))
print(sol.allCellsDistOrderSort(rows = 2, cols = 2, rCenter = 0, cCenter = 1))
print(sol.allCellsDistOrderSort(rows = 2, cols = 3, rCenter = 1, cCenter = 2))