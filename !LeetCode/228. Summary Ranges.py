from tkinter import N
from typing import List


class Solution:
    # Iterate through detecting start and end points.
    # Print as single number if those numbers are the same,
    # or print as range if different.
    # O(n) time.
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        start, stop, res = None, None, []

        def printRange():
            if start == stop or stop is None:
                res.append(str(start))
            else:
                res.append("".join([str(start), "->", str(stop)]))

        for i, n in enumerate(nums):
            if i == 0:
                start = n

            if i > 0 and n != (nums[i - 1] + 1):  # Print if discontinuity is detected
                stop = nums[i - 1]
                printRange()
                start, stop = n, None

            if i == len(nums) - 1:  # Print when reaching last number
                stop = n
                printRange()

        return res


sol = Solution()
print(sol.summaryRanges(nums=[-1]))
print(sol.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
print(sol.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
