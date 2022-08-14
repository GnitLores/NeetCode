from typing import List


class Solution:
    # If the subarray has a negative prefix, it can be discarded.
    # Iterate through the array. When a negative prefix is detected:
    # Reset the current sum and start adding from zero again.
    # At each step record the maximum sum.
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0

        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n

            maxSum = max(maxSum, currentSum)

        return maxSum

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))