from math import ceil
class Solution(object):
    # Popping the elements visited might not be the most efficient,
    # but it makes it easy to understand the code and has same time complexity.
    # We need some checks to unsure that there are still elements left because the input needs not be quadratic.
    # O(n*m)
    def spiralOrder(self, matrix):
        res = []

        while len(matrix) > 1:
            res = res + matrix.pop(0) # Add top row to output.
            bottomRow = matrix.pop(-1) # Remove bottom row from matrix and store
            
            # Add right column in descending order
            if matrix and matrix[0]:
                for r in range(len(matrix)):
                    res.append(matrix[r].pop(-1))

            # Add stored bottom row to output but mirrored
            bottomRow.reverse()
            res = res + bottomRow
            
            # Add left column in ascending order
            if matrix and matrix[0]:
                for r in range(len(matrix)-1,-1,-1):
                    res.append(matrix[r].pop(0))

        # If these is an odd number of rows, add the remaining row.
        if matrix:
            res = res + matrix.pop(0)

        return res

sol = Solution()
print(sol.spiralOrder([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]))

print(sol.spiralOrder([
    [7],
    [9],
    [6]]))

print(sol.spiralOrder([
    [1,2,3],
    [4,5,6],
    [7,8,9]]))
print("")
print(sol.spiralOrder([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]))
print("")
print(sol.spiralOrder([
    [1,2,3],
    [4,5,6],
    [7,8,9]]))
    