import collections
from typing import List


class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = collections.defaultdict(int)
        rows = len(matrix)
        cols = len(matrix[0])
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(coords):
            if coords in memo:
                return memo[coords]
            
            path = 1
            r, c = coords
            for dr, dc in dirs:
                rn, cn = r + dr, c + dc
                if 0 <= rn < rows and 0 <= cn < cols:
                    if matrix[rn][cn] < matrix[r][c]:
                        path = max(path, 1 + dfs((rn, cn)))
            memo[coords] = path
            return path

        maxPath = 0
        for r in range(rows):
            for c in range(cols):
                maxPath = max(maxPath, dfs((r, c)))
        return maxPath

sol = Solution()
print(sol.longestIncreasingPath(matrix = [
    [9,9,4],
    [6,6,8],
    [2,1,1]]))
print(sol.longestIncreasingPath([
    [3,4,5],
    [3,2,6],
    [2,2,1]]))
print(sol.longestIncreasingPath(matrix = [
    [1]]))
print("")