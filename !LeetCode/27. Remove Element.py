from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """ Modify array in place with O(1) memory """

        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            if nums[l] != val:
                l += 1
        cnt = 0
        for n in nums:
            if n != val:
                cnt += 1

        return cnt

sol = Solution()
print(sol.removeElement([1,1,1], val = 1))
print(sol.removeElement([1,], val = 1))
print(sol.removeElement([3,2,2,3], val = 3))
print(sol.removeElement([0,1,2,2,3,0,4,2], val = 2))