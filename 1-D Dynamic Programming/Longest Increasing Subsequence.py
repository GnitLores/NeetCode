from typing import List


class Solution:
    # Dynamic programming solution.
    # Iterate backwards and memo the LIS starting at each index.
    # For each iteration start a forward iterating seach for numbers greater than the current number.
    # The LIS is the max LIS for numbers greater the current number + 1.
    # There are also nlog(n) solutions, but they are too complex to solve in a limited time.
    # O(n^2) time.
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):

            for k in range(i + 1, len(nums)):
                if nums[i] < nums[k]:
                    dp[i] = max(dp[i], dp[k] + 1)

        return max(dp)

sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS([0,1,0,3,2,3]))
print(sol.lengthOfLIS([7,7,7,7,7,7,7]))