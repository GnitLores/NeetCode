# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF
# as you may assume that the distance to a gate is less than 2147483647.
#
# Fill each empty room with the distance to its nearest gate.
# If it is impossible to reach a Gate, that room should remain filled with INF
from typing import List
import collections

class Solution:
    # Solution using BFS.
    # identify all walls and start a BFS from each.
    # Carry out BFS in rounds, incrementing the distance with each round.
    # Overwrite the disatance in the array.
    # Of a shorter distance is encountered, stop the BFS there. It is already as close or closer to a gate.
    # Should be O(gates*m*n) time worst case.

    def walls_and_gates(self, rooms: List[List[int]]):
        rows = len(rooms)
        cols = len(rooms[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c):
            queue = collections.deque()
            queue.append((r,c))

            dist = 0
            while queue:
                dist += 1
                for _ in range(len(queue)): # Carry out round of searching before incrementing distance.
                    r, c = queue.popleft()

                    for dr, dc in directions:
                        rn = r + dr
                        cn = c + dc

                        if rn in range(rows) and cn in range(cols):
                            if rooms[rn][cn] > 0 and dist < rooms[rn][cn]: # Stop if wall or gate or not a path at greater distance from gate than this.

                                rooms[rn][cn] = min(dist, rooms[rn][cn])
                                queue.append((rn,cn))

        # Find all gates
        gates = []
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    gates.append((r, c))
        
        if len(gates) == 0:
            return

        for r, c in gates:
            bfs(r, c)

        print("")
        for r in range(rows):
            print(rooms[r])

sol = Solution()

# the 2D grid is:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
board = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]]
sol.walls_and_gates(board)