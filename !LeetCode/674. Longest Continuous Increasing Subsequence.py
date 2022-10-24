from typing import List


class Solution:
    # Iterate through and detect breaks in increasing sequence
    # and record max length on breaks.
    # The end of the array is also a break.
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res, length = 0, 0
        for i, n in enumerate(nums):
            length += 1
            if i == len(nums) - 1 or n >= nums[i + 1]:
                res = max(res, length)
                length = 0
        return res

sol = Solution()
print(sol.findLengthOfLCIS(nums = [1,3,5,4,7]))
print(sol.findLengthOfLCIS(nums = [2,2,2,2,2]))