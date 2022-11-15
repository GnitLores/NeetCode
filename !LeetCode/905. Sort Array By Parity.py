from typing import List


class Solution:
    # Two pointer solution.
    # Continously find odd values with left pointer and even values with right pointer
    # and swap them until pointers meet.
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] % 2 == 0: l += 1
            while l < r and nums[r] % 2 == 1: r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        return nums

sol = Solution()
print(sol.sortArrayByParity(nums = [3,1,2,4]))
print(sol.sortArrayByParity(nums = [0]))