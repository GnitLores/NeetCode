from typing import List


class Solution:
    # For any house the robber can decide between ither the sum
    # of that house plus what they would have robbing the house two places back,
    # or what they would have after robbing the previous house and not this one.
    # O(n) time.
    def rob(self, nums: List[int]) -> int:
        twoAgo = 0
        oneAgo = 0

        for i in range(len(nums)):
            nums[i] = max(twoAgo + nums[i], oneAgo)
            twoAgo = oneAgo
            oneAgo = nums[i]

        return nums[-1]


sol = Solution()
print(sol.rob([1,2,3,1]))
print(sol.rob([2,7,9,3,1]))