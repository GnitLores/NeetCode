from typing import List


class Solution:
    # We can check if the slope between points 1 and 2 and the slope bewteen points 1 and 3
    # are the same. If both slopes are the same, the points are on a straight line.
    # However, calculating the slope runs the risk of dividing by zero if the points are
    # vertically above one another. To avoid this we can multiply by the divisors on both sides
    # of the equality:
    # slope1 = (p1[1] - p2[1]) / (p1[0] - p2[0])
    # slope2 = (p1[1] - p3[1]) / (p1[0] - p3[0])
    # sameSlope = slope1 == slope2
    # sameSlope = (p1[1] - p2[1]) / (p1[0] - p2[0]) == (p1[1] - p3[1]) / (p1[0] - p3[0])
    # sameSlope = (p1[1] - p2[1]) * (p1[0] - p3[0]) == (p1[1] - p3[1]) * (p1[0] - p2[0])
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1, p2, p3 = points
        return not (p1[1] - p2[1]) * (p1[0] - p3[0]) == (p1[1] - p3[1]) * (p1[0] - p2[0])

sol = Solution()
print(sol.isBoomerang(points = [[1,1],[2,3],[3,2]]))
print(sol.isBoomerang(points = [[1,1],[2,2],[3,3]]))