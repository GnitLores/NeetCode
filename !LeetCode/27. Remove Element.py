from typing import List


class Solution:
    # Two pointer solution.
    # Maintain pointer to left and right side.
    # If left is the target value, swap it for the right pointer value
    # and move the right pointer left.
    # If the right value was also the target value, sweap again, otherwise
    # move the left pointer right.
    # Count the elements not equal to val.
    # O(n) time and O(1) space.
    def removeElement(self, nums: List[int], val: int) -> int:
        """Modify array in place with O(1) memory"""

        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            if nums[l] != val:
                l += 1
        return sum(n != val for n in nums)


sol = Solution()
print(sol.removeElement([1, 1, 1], val=1))
print(sol.removeElement([1], val=1))
print(sol.removeElement([3, 2, 2, 3], val=3))
print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], val=2))
