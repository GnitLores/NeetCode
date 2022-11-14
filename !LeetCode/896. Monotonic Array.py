from typing import List


class Solution:
    # Start by finding the difference between the first and last element to determine the overall directionality.
    # Compare all adjacent elements.
    # If they are identical, they are always valid. If all elements are identical we will never consider directionality.
    # Consequently we can assume that the directionality is either negative or positive in the following operation.
    # If we ever encounter a local change in direction that is different from the overall direction, this violates the monotonic property.
    # Use XOR between global and local directionality to determine if they ever disagree.
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return True
        shouldIncrease = nums[-1] - nums[0] > 0
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]: continue
            direction = nums[i - 1] < nums[i]
            if shouldIncrease ^ direction: return False
        return True

sol = Solution()
print(sol.isMonotonic(nums = [1,2,2,3]))
print(sol.isMonotonic(nums = [6,5,4,4]))
print(sol.isMonotonic(nums = [1,3,2]))