from typing import List


class Solution:
    # Iterate throguh tracking left and right sums divided by pivot.
    # Subtract current number from right sum, which is initialized
    # to the sum of the full array.
    # Add previous number to left sum.
    # THe pivot point itself is never part of either sum, it is added to the
    # left sum on the next iteration, when it is no longer the pivot.
    # If sums are equal, this is a valid pivot.
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        for i, n in enumerate(nums):
            rightSum -= n
            if i > 0: leftSum += nums[i - 1]
            if leftSum == rightSum: return i
        return -1

sol = Solution()
print(sol.pivotIndex(nums = [1,7,3,6,5,6]))
print(sol.pivotIndex(nums = [1,2,3]))
print(sol.pivotIndex(nums = [2,1,-1]))