from typing import List
from itertools import accumulate

# If we just store the numbers, quering a range would be N(range) time.
# However, we can make the queries constant time by storing the numbers as an
# accumulated sum at the cost of making creating the array linear time.
# Since there should be many more queries, this is well worth it.
# The sum of the range is the accumulated sum at the right pointer, minus
# the accumulated sum before the left pointer (0 if left pointer is at 0).
# Query = O(1) time.
class NumArray:
    def __init__(self, nums: List[int]):
        self.cumSum = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.cumSum[right]
        return self.cumSum[right] - self.cumSum[left - 1]
        


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))