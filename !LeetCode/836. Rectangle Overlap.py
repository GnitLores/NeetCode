from typing import List


class Solution:
    # Check if the rectangles are overlapping in their projection on the x and y axes.
    # If both projections are overlapping, the rectangles overlap.
    # If for example they are overlapping in their projection on the x axis but not on
    # the y axis, they are just located above and below one another and are not overlapping.
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1a, y1a, x2a, y2a = rec1
        x1b, y1b, x2b, y2b = rec2

        overlapX = not (x2a <= x1b or x1a >= x2b)
        overlapY = not (y2a <= y1b or y1a >= y2b)
        
        return overlapX and overlapY

sol = Solution()
print(sol.isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3]))
print(sol.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [1,0,2,1]))
print(sol.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [2,2,3,3]))