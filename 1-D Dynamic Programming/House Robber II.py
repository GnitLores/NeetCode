from typing import List


class Solution:
    # Reusing the solution from House Robber.
    # Since we know that the first and last houses cannot both be chosen,
    # we can carry out two attemps - one with each of those houses omitted.
    # The best choice is the one that gives the max value.
    # O(n) time.
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robSection(nums):
            twoAgo = 0
            oneAgo = 0

            for i in range(len(nums)):
                nums[i] = max(twoAgo + nums[i], oneAgo)
                twoAgo = oneAgo
                oneAgo = nums[i]

            return nums[i]

        ignoreLast = robSection(nums[:-1]) # Omit last house
        ignoreFIrst = robSection(nums[1:]) # Omit first house
        return max(ignoreLast, ignoreFIrst)

sol = Solution()
print(sol.rob([2,3,2]))
print(sol.rob([1,2,3,1]))
print(sol.rob([1,2,3]))