class Solution(object):
    def rotate(self, matrix):
        for row in matrix:
            print(row)

        rows = len(matrix)
        cols = len(matrix[0])

        r = 0
        for c in range(cols-1):
            val = matrix[r][c]
            for _ in range(4):
                val, matrix[c][-1-r] = matrix[c][-1-r], val
                r, c = c, -1-r

        print("")
        for row in matrix:
            print(row)

sol = Solution()
sol.rotate([
    [1,2,3],
    [4,5,6],
    [7,8,9]])