from typing import List


class Solution:
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