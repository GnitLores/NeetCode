from typing import List
import collections

# BFS solution.
# We don't brute force a search from all locations.
# Instead we start from the edges and find locations that we can move UP.
# Visited notes get added to sets, one for each ocean.
# Start a bfs from each edge location, upper and left edge for pacific, lower and right for atlantic.
# Finally intersect sets to find coordinates of locations reachable from both oceans.
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacificVisit = set()
        atlanticVisit = set()
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def bfs(r, c, visit):
            if (r, c) in visit:
                return
            queue = collections.deque()
            queue.append((r, c))
            visit.add((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols): 
                        if (r, c) not in visit and heights[r][c] >= heights[row][col]:
                            queue.append((r, c))
                            visit.add((r, c))


        for c in range(cols):
            bfs(0, c, pacificVisit)
            bfs(rows-1, c, atlanticVisit)
        for r in range(rows):
            bfs(r, 0, pacificVisit)
            bfs(r, cols-1, atlanticVisit)

        valid = atlanticVisit.intersection(pacificVisit)
        res = []
        for n in valid:
            res.append(list(n))
        res.sort()
        return res

sol = Solution()
heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]]
print(sol.pacificAtlantic(heights))