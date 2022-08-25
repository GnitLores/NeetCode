from typing import List

class Solution:
    # Dynamic programming solution. Recursive top down solution with caching.
    #
    # We can always be in one of two states (in addition to being forced to wait after selling).
    # If we have not bought, then we can only buy or wait.
    # If we have bought, then we can only either sell or wait.
    # Thus there is only at most two decisions per branch in the decision tree, and the recursion relation is:
    # Can buy - the max of either (buying today + max profit being in selling state next day) and (waiting and being in buying state next day)
    # Can sell - the max of either (selling today + max profit of being in buying state in two days) and (waiting and being in buysing state next day)
    # An extra cooldown day must pass after selling.
    # We can do a dfs through the decision tree and cache the results for each day with a hashset using a tuple key (i, canBuy).
    # There are at most 2 * n possible distinct subproblem results, so with caching this is linear time.
    #
    # O(n) time.

    def maxProfit(self, prices: List[int]) -> int:
        cache = dict()

        def dfs(i, canBuy):
            if i >= len(prices): return 0
            if (i, canBuy) in cache: return cache[(i, canBuy)]

            waitProfit = dfs(i + 1, canBuy)
            if canBuy:
                buyProfit = dfs(i + 1, not canBuy) - prices[i]
                cache[(i, canBuy)] = max(buyProfit, waitProfit)
            else:
                sellProfit = dfs(i + 2, not canBuy) + prices[i]
                cache[(i, canBuy)] = max(sellProfit, waitProfit)
            return cache[(i, canBuy)]

        canBuy = True
        return dfs(0, canBuy)

sol = Solution()
print(sol.maxProfit([1,2,3,0,2]))
print(sol.maxProfit([1]))