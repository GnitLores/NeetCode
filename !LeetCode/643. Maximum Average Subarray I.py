from typing import List


class Solution:
    # Sliding window solution.
    # To avoid calculating the entire window on every iteration we just subtract
    # the first value and add the next value to the sum as we move the window.
    # There is no need to calculate the average on every iteration, we can just
    # find the max sum and then divide that by k, This avoids having to divide on
    # every iteration.
    # O(n) time.
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        winSum = sum(nums[:k])
        maxSum = winSum

        # Move the sliding window as many times as there are values not in the window.
        for i in range(len(nums) - k):
            winSum -= nums[i]
            winSum += nums[i + k]
            maxSum = max(maxSum, winSum)

        return maxSum / k

sol = Solution()
print(sol.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
print(sol.findMaxAverage(nums = [5], k = 1))