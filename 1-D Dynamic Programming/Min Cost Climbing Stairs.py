from typing import List


class Solution:
    # Each step can only be reached from the two steps below it.
    # Thus the optimal choice if you are using this step, is to go from the step with lower cost.
    # The cost of stepping from each step is the min cost of stepping from the two lower steps
    # plus the cost of the step itself.
    # O(n) time.
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = 0 + cost[0]
        dp[1] = min(0, cost[0]) + cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]


        return min(dp[-1], dp[-2])

    # Solution using constant space and working from right to left.
    # Otherwise the method is identical.
    # O(n) time.
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

sol = Solution()
print(sol.minCostClimbingStairs([10,15,20]))
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))