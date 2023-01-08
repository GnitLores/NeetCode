from importlib.metadata import entry_points
from typing import List


class Solution:
    # The first part of the array must be unique elements.
    # Everything after that doesn't matter.
    # Increment insertion index and insert new values at
    # that index.
    # Don't increment index for duplicate values.
    def removeDuplicates(self, nums: List[int]) -> int:
        insertIndex = 1
        uniqueNums = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insertIndex] = nums[i]
                insertIndex += 1
                uniqueNums += 1
        return uniqueNums


sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))
print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
