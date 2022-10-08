from typing import List


class Solution:
    # Calculate triangle line by line and store only the previous row.
    # since only two rows are stored at any time and each row is as long as
    # its index + 1, we use only O(2*rowIndex) = O(rowIndex) space.
    def getRow(self, rowIndex: int) -> List[int]:
        """ Use only O(rowIndex) extra space """
        row, prevRow = [1], [0, 1, 0]
        for r in range(1, rowIndex + 1):
            row = []
            for i in range(0, r + 1):
                row.append(prevRow[i] + prevRow[i + 1])
            prevRow = [0] + row + [0]
        return row

sol = Solution()
print(sol.getRow(rowIndex = 3))
print(sol.getRow(rowIndex = 0))
print(sol.getRow(rowIndex = 1))