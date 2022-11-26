import heapq
from typing import List


class Solution:
    # We will always want to negate the lowest value in the array.
    # The more negative it is, the more negating it will contribute,
    # and if there are no negative values, the lower the value is, the less
    # negating it will subtract from the sum.
    # Consequently, we can heapify the array and k times pop the lowest value
    # and push the negated value back on the heap.
    # The resulting array has the largest sum possible.
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heappush(nums, -heapq.heappop(nums))
        return sum(nums)


sol = Solution()
print(sol.largestSumAfterKNegations(nums = [4,2,3], k = 1))
print(sol.largestSumAfterKNegations(nums = [3,-1,0,2], k = 3))
print(sol.largestSumAfterKNegations(nums = [2,-3,-1,5,-4], k = 2))