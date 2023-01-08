from typing import List


class Solution:
    # Binary search solution.
    # O(logn)
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m  # Return place if found
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        # If not found, if the number is smaller than the closest element, it would take it's place if inserted.
        return m if target < nums[m] else m + 1


sol = Solution()
print(sol.searchInsert(nums=[1, 3, 5, 6], target=5))
print(sol.searchInsert(nums=[1, 3, 5, 6], target=2))
print(sol.searchInsert(nums=[1, 3, 5, 6], target=7))
