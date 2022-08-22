from typing import List
import collections 

# Observation, since we are looking for squares with even sides, the point located
# diagonally across must be exactly as distant in x as it is distant in y.
# In addition, the distance must be greater than 0.
# This means that we can just look through all points in linear time and look for
# points that fulfill these criteria.
# For each point that does, we can then calculate the amount of combinations for
# that point, by looking up the count of point at the other two corners in a dictionary.
# O(n) time.
class DetectSquares:
    def __init__(self):
        self.ptsCount = collections.defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1 # Count points
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if abs(py - y) == abs(px - x) and x-px != 0: # If valid point diagonally across from input
                res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)] # Add combinations for that point given count of other corner points
        return res

detectSquares = DetectSquares()
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])
print(detectSquares.count([11, 10])) # return 1. You can choose:
                                     #   - The first, second, and third points
print(detectSquares.count([14, 8]))  # return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2])           # Adding duplicate points is allowed.
print(detectSquares.count([11, 10])) # return 2. You can choose:
                                     #   - The first, second, and third points
                                     #   - The first, third, and fourth points