from cmath import sqrt
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(x**2 + y**2) for x, y in points] # Real calculation is (x**2 + y**2)**0.5, but taking the square root to find the true distance will not change the ordering.
        dist = list(zip(dist, points))
        heapq.heapify(dist)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(dist)[1])
        return res

sol = Solution()
print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))