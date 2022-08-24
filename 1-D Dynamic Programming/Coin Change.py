from typing import List


class Solution:
    # Dynamic programming solution.
    # For each possible value up the final value, memoize what the minimum number of coins to reach it is.
    # For each coin, read that number was for the value that adding the coin to would give the current value.
    # Then find the minimum of those and add 1 coin.
    # O(coins * amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        placeholder = amount + 1
        dp = [placeholder] * (amount + 1)
        dp[0]= 0
        for val in range(1, amount + 1):
            for coin in coins:
                if val - coin >= 0:
                    dp[val] = min(dp[val], dp[val - coin] + 1)

        return dp[-1] if dp[-1] != placeholder else -1

sol = Solution()
print(sol.coinChange([1,2,5], 11))
print(sol.coinChange([2], 3))
print(sol.coinChange([1], 0))