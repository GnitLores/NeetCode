class Solution(object):
    # Solution using hashsets.
    # Search through and store coordinates of 0s in hashsets.
    # Then for each coordinate, zero out that row/column.
    # Prevents repeated work.
    # O(m*n) time.
    # This uses O(n+m) extra space.
    # It could be done in O(1) by indicating columns to zero in tow row and rows to zero in left column.
    # It would make the code a bit more complicated though.
    def setZeroes(self, matrix):
        print("")
        for row in matrix:
            print(row)

        rows = set()
        cols = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        
        for r in rows:
            matrix[r] = [0]*len(matrix[0])
        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0

        print("")
        for row in matrix:
            print(row)

sol = Solution()
sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])