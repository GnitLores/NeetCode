from typing import List


class Solution:
    # Solution using a helper function that checks if the diagonal
    # sloping down and to the right from any point contains only a single value.
    # Execute this function from all leftmost elements and for all top elements
    # (but only once from the top leftmost element), and check if any diagonal is
    # invalid.
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        def diagonalIsValid(row, col):
            val = matrix[row][col]
            r, c = row + 1, col + 1
            while r < rows and c < cols:
                if matrix[r][c] != val: return False
                r += 1
                c += 1
            return True

        for row in range(rows):
            if not diagonalIsValid(row, 0): return False
        for col in range(1, cols):
            if not diagonalIsValid(0, col): return False     
        return True

sol = Solution()
print(sol.isToeplitzMatrix(matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(sol.isToeplitzMatrix(matrix = [[1,2],[2,2]]))