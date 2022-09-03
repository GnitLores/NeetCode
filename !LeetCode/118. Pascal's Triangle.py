from typing import List


class Solution:
    # Iteratively fill in by adding 1 at the edges and 
    # summing elements from the previous row.
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for r in range(numRows):
            if r == 0:
                res.append([1])
                continue

            row = []
            for i in range(r + 1):
                if i == 0 or i == r:
                    row.append(1)
                else:
                    row.append(res[r - 1][i - 1] + res[r - 1][i])
            res.append(row)
        return res
        

sol = Solution()
print(sol.generate(5))
print(sol.generate(1))