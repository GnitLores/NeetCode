from typing import List


class Solution:
    # Create a matrix of transposed dimensions and insert all elements with
    # row and column indices swapped.
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = [[None] * rows for c in range(cols)]
        for r in range(rows):
            for c in range(len(matrix[0])):
                res[c][r] = matrix[r][c]
        return res

sol = Solution()
print(sol.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(sol.transpose(matrix = [[1,2,3],[4,5,6]]))