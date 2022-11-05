class Solution:
    # The area of a triangle in coordinate geometry can be calculated
    # as the area of the two trapezoids spanning from the x axis and covering
    # the triangle minus the area of the trapezoid between the triangle and the
    # x axis.
    # This reduces to the formula abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        res = 0
        nPoints = len(points)
        for i in range(nPoints):
            x1, y1 = points[i]
            for j in range(i + 1, nPoints):
                x2, y2 = points[j]
                for k in range(j + 1, nPoints):
                    x3, y3 = points[k]
                    a = x1 * (y2 - y3)
                    b = x2 * (y3 - y1)
                    c = x3 * (y1 - y2)
                    area = abs(0.5 * (a + b + c))
                    res = max(res, area)
        return res

sol = Solution()
print(sol.largestTriangleArea(points = [[0,0],[0,1],[1,0],[0,2],[2,0]]))
print(sol.largestTriangleArea(points = [[1,0],[0,0],[0,1]]))