import collections
from typing import List
import heapq

class Solution:
    # Solution using BFS.
    # Iteratively try to reach the target as the water rises.
    # It would be inefficient to do a full BFS for every iteration,
    # so store a set of visited tiles and never visit them again.
    # However, this leads to a problem - where to start subsequent BFS attempts.
    # We cannot start from a tile we have already visited, and it is likely that
    # any path to the target will be blocked by visited tiles.
    # To solve this, we create a frontier with a dictionary, mapping times t
    # to tile positions.
    # Whenever we encounter a tile that is too high to reach, add it to the frontier.
    # When t reaches h, start a BFS from each tile in frontier[h].
    # This way we guarantee that we will never visit a tile twice, and that we will reach
    # the target as early as possible.

    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        frontier = collections.defaultdict(set)
        
        queue = collections.deque()
        visited = set()

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(r, c, t):
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                r, c = queue.popleft()

                if (r == rows - 1) and (c == cols - 1):
                    return True

                for dr, dc in dirs:
                    rNew = r + dr
                    cNew = c + dc
                    if (0 <= rNew < rows) and (0 <= cNew < cols) and ((rNew, cNew) not in visited):
                        height = grid[rNew][cNew]
                        if height <= t: # If the tile is reachable, add it to the queue
                            queue.append((rNew, cNew))
                            visited.add((rNew, cNew))
                        else: # Otherwise add it to the frontier
                            frontier[height].add((rNew, cNew))

            return False
        
        t = max(grid[0][0], grid[-1][-1]) # It is impossible to reach the goal before both the first and last tile are underwater.
        frontier[t].add((0, 0))
        while True:
            if frontier[t]:
                for r, c in frontier[t]:
                    if bfs(r, c, t):
                        return t
            t += 1

    # Neetcode solution.
    # Modified version of Dijkstra's algorithm using BFS and minheap.
    # For the frontier, use a minheap of tiles ordered by height.
    # Instead of iterating over t, just set t to the height currently popped
    # from the heap and being visited.
    # When adding a tile, set height to max(t, tileheight) in order to make
    # each tile as heigh as the highest tile blocking it on the path.
    # This is the earliest time at which we can visit it.
    
    def swimInWaterDijkstra(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (
                    neiR < 0
                    or neiC < 0
                    or neiR == N
                    or neiC == N
                    or (neiR, neiC) in visit
                ):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])

sol = Solution()
print(sol.swimInWater(grid = [
    [0,2],
    [1,3]]))
print(sol.swimInWater(grid = [
    [0,1,2,3,4],
    [24,23,22,21,5],
    [12,13,14,15,16],
    [11,17,18,19,20],
    [10,9,8,7,6]]))
print(sol.swimInWater(grid = [
    [7,23,21,9,5],
    [3,20,8,18,15],
    [14,13,1,0,22],
    [2,10,24,17,12],
    [6,16,19,4,11]]))
print(sol.swimInWater([
    [281,116,221,293,132,29,66,150,332,371,35,211,70,111,229,59,284,303,295,275],
    [147,268,209,55,186,182,309,80,321,176,26,106,124,270,97,9,76,367,91,198],
    [334,93,345,68,264,348,125,22,316,100,323,285,139,138,171,305,223,343,61,127],
    [386,390,119,189,53,21,302,379,102,286,178,243,19,47,258,216,151,165,292,225],
    [10,153,269,358,43,219,374,217,39,110,256,393,257,56,3,1,77,331,262,8],
    [315,364,385,123,113,215,96,350,5,330,326,16,194,212,299,240,73,31,17,380],
    [90,395,191,359,328,183,342,129,370,300,341,193,130,336,136,81,314,347,161,238],
    [63,253,200,288,4,236,36,67,37,48,294,201,242,369,157,357,109,57,271,327],
    [34,38,126,389,325,72,104,143,196,142,372,205,108,62,146,365,101,207,333,272],
    [112,64,313,383,75,180,163,179,44,181,197,133,32,228,233,248,363,86,78,71],
    [121,296,30,158,301,54,202,349,7,324,195,399,226,277,340,103,33,263,117,20],
    [361,154,58,368,266,144,185,274,306,51,234,311,40,308,69,261,344,307,338,280],
    [120,28,159,366,237,339,74,394,235,250,95,164,329,24,60,310,149,156,252,192],
    [18,273,52,172,65,247,276,177,206,175,79,346,279,122,298,230,82,188,135,377],
    [184,254,115,382,208,45,137,145,396,42,224,373,241,169,199,107,337,12,134,174],
    [391,322,381,290,49,388,278,203,105,173,232,85,351,168,0,11,239,319,312,282],
    [128,289,318,15,166,89,162,46,25,317,297,356,99,304,148,152,141,249,98,245],
    [265,259,87,392,140,220,14,227,213,320,251,155,255,231,210,246,83,244,27,131],
    [190,378,291,204,267,260,360,376,6,170,13,214,187,362,94,352,283,397,218,353],
    [92,2,387,222,160,384,50,114,88,335,375,167,84,355,354,118,287,41,23,398]]))

print("")
print(sol.swimInWaterDijkstra(grid = [
    [0,2],
    [1,3]]))
print(sol.swimInWaterDijkstra(grid = [
    [0,1,2,3,4],
    [24,23,22,21,5],
    [12,13,14,15,16],
    [11,17,18,19,20],
    [10,9,8,7,6]]))
print(sol.swimInWaterDijkstra(grid = [
    [7,23,21,9,5],
    [3,20,8,18,15],
    [14,13,1,0,22],
    [2,10,24,17,12],
    [6,16,19,4,11]]))
print(sol.swimInWaterDijkstra([
    [281,116,221,293,132,29,66,150,332,371,35,211,70,111,229,59,284,303,295,275],
    [147,268,209,55,186,182,309,80,321,176,26,106,124,270,97,9,76,367,91,198],
    [334,93,345,68,264,348,125,22,316,100,323,285,139,138,171,305,223,343,61,127],
    [386,390,119,189,53,21,302,379,102,286,178,243,19,47,258,216,151,165,292,225],
    [10,153,269,358,43,219,374,217,39,110,256,393,257,56,3,1,77,331,262,8],
    [315,364,385,123,113,215,96,350,5,330,326,16,194,212,299,240,73,31,17,380],
    [90,395,191,359,328,183,342,129,370,300,341,193,130,336,136,81,314,347,161,238],
    [63,253,200,288,4,236,36,67,37,48,294,201,242,369,157,357,109,57,271,327],
    [34,38,126,389,325,72,104,143,196,142,372,205,108,62,146,365,101,207,333,272],
    [112,64,313,383,75,180,163,179,44,181,197,133,32,228,233,248,363,86,78,71],
    [121,296,30,158,301,54,202,349,7,324,195,399,226,277,340,103,33,263,117,20],
    [361,154,58,368,266,144,185,274,306,51,234,311,40,308,69,261,344,307,338,280],
    [120,28,159,366,237,339,74,394,235,250,95,164,329,24,60,310,149,156,252,192],
    [18,273,52,172,65,247,276,177,206,175,79,346,279,122,298,230,82,188,135,377],
    [184,254,115,382,208,45,137,145,396,42,224,373,241,169,199,107,337,12,134,174],
    [391,322,381,290,49,388,278,203,105,173,232,85,351,168,0,11,239,319,312,282],
    [128,289,318,15,166,89,162,46,25,317,297,356,99,304,148,152,141,249,98,245],
    [265,259,87,392,140,220,14,227,213,320,251,155,255,231,210,246,83,244,27,131],
    [190,378,291,204,267,260,360,376,6,170,13,214,187,362,94,352,283,397,218,353],
    [92,2,387,222,160,384,50,114,88,335,375,167,84,355,354,118,287,41,23,398]]))