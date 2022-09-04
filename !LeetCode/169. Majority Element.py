import collections
from typing import List


class Solution:
    # Count numbers with dictionary and return number if count is greater than half the size.
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        half = len(nums) // 2
        for n in nums:
            count[n] += 1
            if count[n] > half:
                return n

sol = Solution()
print(sol.majorityElement([3,2,3]))
print(sol.majorityElement([2,2,1,1,1,2,2]))