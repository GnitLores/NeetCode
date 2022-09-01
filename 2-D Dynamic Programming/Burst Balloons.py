from typing import List


class Solution:
    # Neetcode's solution using recursion with memoization.
    # The key trick is not to look for what happens when you pop a balloon first,
    # but when you pop it LAST.
    # If you pop it first, the array changes, but when you pop it last, you essentially
    # divide the array into left and right subarrays.
    # We just need to keep in mind the edges, so we insert a 1 on either side of the array,
    # and the balloon popped last will be included when popping the inner edge balloon in each subarray.
    # The maximal number of coins is the max number gained when popping each of the n balloons last.
    # Carry out a depth first search for each of those options, dividing the array into left and right halves
    # with l and r pointer and an iterator i.
    # Recursively do the same for those subarrays, and store the intermediate subproblem results in a cache.
    # O(n^3) time since the cache contains results for O(n^2) subarrays and we iterate trough all subarrays.
    # This solution actually does not pass the new test cases on leetcode.
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1] # For edge balloons, will include dummy 1s on sides and/or balloon being popped last
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[l, r], coins)
            return dp[(l, r)]


        res = dfs(1, len(nums) - 2)
        return res

sol = Solution()
print(sol.maxCoins(nums = [3,1,5,8]))
print(sol.maxCoins(nums = [1,5]))