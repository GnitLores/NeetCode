from typing import List


class Solution:
    # Recursive search with caching.
    # When you add another number, it can either be negative or positive.
    # Thus, the amount of ways to reach the target is the amount of ways to reach
    # the target +/- that number without the number included.
    # If we include numbers up to i, the recurrence relation is:
    # ways(i, sum) = ways(i-1, sum+nums[i]) + ways(i-1, sum-nums[i])
    # Once we reach 0 numbers included, there is exactly one way to reach a sum of zero,
    # and zero ways to reach any other sum.
    # O(n * sum(nums)) time.
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = dict()

        def dfs(i, s):
            if (i, s) in cache: return cache[(i, s)]
            
            if i == -1:
                cache[(i, s)] = 1 if s == 0 else 0
                return cache[(i, s)]

            res = dfs(i - 1, s - nums[i]) + dfs(i - 1, s + nums[i])
            cache[(i, s)] = res
            return res

        return dfs(len(nums) - 1, target)

    # Dynamic programming implementation with an array.
    # Runs a bit slower, probably because sum can get large.
    # Could probably be made much more efficient by only including either positive or negative side,
    # and by only including the previous column and not the whole table.
    # O(n * sum(nums)) time.
    def findTargetSumWaysDP(self, nums: List[int], target: int) -> int:
        if abs(target) > sum(nums):
            return 0 
        if len(nums) == 1:
            if nums[0] == 0:
                return 2
            else:
                return 1

        maxNum = sum(nums)
        sumRange = range(-maxNum, maxNum + 1)
        dp = [[0] * (len(nums) + 2) for _ in sumRange]
        for i, s in enumerate(sumRange):
            dp[i][-1] = s
        
        for k in range(len(nums) + 1):
            n = nums[k - 1]
            for i, s in enumerate(sumRange):
                if k == 0:
                    dp[i][k] = 1 if s == 0 else 0
                    continue

                if s + n in sumRange:
                    dp[i][k] += dp[i + n][k - 1]
                
                if s - n in sumRange:
                    dp[i][k] += dp[i - n][k - 1]
        
        return dp[sumRange.index(target)][-2]

        

sol = Solution()
print(sol.findTargetSumWays([1,1,1,1,1], 3))
print(sol.findTargetSumWays([1], 1))
print(sol.findTargetSumWays([1], 2))
print(sol.findTargetSumWays([1, 0], 1))
print(sol.findTargetSumWays([9,7,0,3,9,8,6,5,7,6], 2))
print("")
print(sol.findTargetSumWaysDP([1,1,1,1,1], 3))
print(sol.findTargetSumWaysDP([1], 1))
print(sol.findTargetSumWaysDP([1], 2))
print(sol.findTargetSumWaysDP([1, 0], 1))
print(sol.findTargetSumWaysDP([9,7,0,3,9,8,6,5,7,6], 2))