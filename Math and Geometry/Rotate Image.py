class Solution(object):
    # Rotate in layers.
    # O(n^2)
    def rotate(self, matrix):
        print("")
        for row in matrix:
            print(row)

        for layer in range(0, len(matrix)//2):  # There are half as many layers as there are rows/columns (rounding down if odd number to exlude center element which remains constant)
            r = layer
            for c in range(layer, len(matrix[0]) -1 -layer): # For each element in the top row of layer (exluding last element which will be replaced by first on rotation):
                val = matrix[r][c] # Store the value
                for _ in range(4): # In four steps:
                    val, matrix[c][-1-r] = matrix[c][-1-r], val # Insert value rotated 90 degrees clockwise and store the value it replaces
                    r, c = c, -1-r # rotate coordinates 90 degrees clockwise

        print("")
        for row in matrix:
            print(row)

sol = Solution()
sol.rotate([
    [1,2,3],
    [4,5,6],
    [7,8,9]])

sol.rotate([
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]])