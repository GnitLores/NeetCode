from typing import List
import math

class Solution:
    # w is always equal to or smaller than the square root
    # of the area, so start searching at the square root.
    # Iteratively decrease w and check if the correct area
    # can be formed with an integer length.
    # Binary search is not possible. We already know what the 
    # optimal ratio would be, but there is no reason that it
    # should be valid.
    def constructRectangle(self, area: int) -> List[int]:
        w = int(math.sqrt(area))
        l = area // w
        while w * l != area:
            w -= 1
            l = area // w
        return [l, w]

sol = Solution()
print(sol.constructRectangle(area = 4))
print(sol.constructRectangle(area = 37))
print(sol.constructRectangle(area = 122122))