from typing import List
import collections

# Solution using breadth first search.
# It is complicated to find surrounded regions.
# Instead we just find edgre regions by running bfs starting along the edges.
# Then we erase the entire board and add the edge regions back in.
# Only the surrounded regions are now gone.
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        edgeRegions = set()

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def bfs(r, c):
            visited = set()
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols):
                        if (r, c) not in visited and board[r][c] == "O":
                            visited.add((r, c))
                            queue.append((r, c))
            return visited
        
        def addEdgeRegion(r, c):
            if (r, c) not in edgeRegions and board[r][c] == "O":
                edgeRegions.update(bfs(r, c))

        # BFS along edges
        for c in range(cols):
            addEdgeRegion(0, c)
            addEdgeRegion(rows-1, c)
        for r in range(rows):
            addEdgeRegion(r, 0)
            addEdgeRegion(r, cols-1)

        # Erase board
        for r in range(rows):
            for c in range(cols):
                board[r][c] = "X"
        
        # Add edge regions back
        for coords in edgeRegions:
            board[coords[0]][coords[1]] = "O"

sol = Solution()
board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]
# Output: [
#     ["X","X","X","X"]
#     ["X","X","X","X"],
#     ["X","X","X","X"],
#     ["X","O","X","X"]]
sol.solve(board)