from typing import List


class Solution:
    # The number of elements in the matrix with the new dimensions must be equal
    # to the number of elements in the old matrix.
    # Iterate through filling out the new matrix.
    # When reaching the end of a row (final column), add a new list to the list of lists and
    # start filling that out from column zero.
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c: return mat
        
        res = []
        row2, col2 = 0, 0
        for row1 in range(len(mat)):
            for col1 in range(len(mat[0])):
                if col2 == c: # Start new row
                    col2 = 0
                    row2 += 1
                if col2 == 0:
                    res.append([])
                res[row2].append(mat[row1][col1])
                col2 += 1

        return res

sol = Solution()
print(sol.matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))
print(sol.matrixReshape(mat = [[1,2],[3,4]], r = 4, c = 1))
print(sol.matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 2))
print(sol.matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4))