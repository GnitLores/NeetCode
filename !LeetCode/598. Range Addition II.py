from typing import List


class Solution:
    # The important thing to realize is that the upper left element
    # is always included in any operation.
    # If an operation includes the element below the top left but not the one to the right,
    # the element to the right can never become a max element again, because
    # any operation that includes it also includes the top left element which is
    # now already greater. Similarly when looking below.
    # This same logic can be extended to the next and then the next element as well.
    #
    # This means that any time an element is exluded from a operation range, there is no
    # operation that will ever make it as great as elements that are already greater and closer
    # to the top left corner. In other words, a max element must be included in ALL operations.
    # Consequently we can just iterate through the operations and find the min row and column included
    # in all operations.
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        maxRow = m
        maxCol = n
        for r, c in ops:
            maxRow = min(maxRow, r)
            maxCol = min(maxCol, c)
        return maxRow * maxCol

sol = Solution()
print(sol.maxCount(m = 3, n = 3, ops = [[2,2],[3,3]]))
print(sol.maxCount(m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]))
print(sol.maxCount(m = 3, n = 3, ops = []))