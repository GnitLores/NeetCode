from typing import List


class Solution:
    # 2-D dynamic programming solution.
    #
    # If we observe the decision tree, at each node we can choose between the coins.
    # However, this results in duplicates since we can choose the same coin multiple times.
    # To avoid duplicates, instead only allow coin and coins to the right in subtree.
    # Example for coins 1, 2, 5: three subtrees, one where 1, 2, 5 is allowed, one
    # where 2, 5 is allowd, and one where only 5 is allowed.
    # This decision tree is at most target amount levels deep (adding all ones to get target).
    # Hence the amount of possible subproblems is (amount * coins).
    # 
    # The recurrence relation depends on whether a coin can be included in the sum.
    # If the coin is <= the target, the number of ways to reach the sum is the number of ways with only coins
    # to the right, plus the number of ways to reach target - coin with this coin included.
    # If the coin is > the target, the number of ways is just the number of ways with only coins to the right.
    #
    # ways(includecoin, amount) = ways(includecoin - 1, amount) + ways(includecoin, amount - coin)
    # ways([1, 2, 5], 5) = ways([2, 5], 5) + ways([1, 2, 5], 4) = 1 + 3 = 4
    #
    # We can memoize the number of ways to reach values in 2D array coins * amount.
    # Each coin row represents not just the coin, but including that coin and coins to the right as before.
    # We initalize an extra column for amount zero which is always 1 (there is one way to reach zero - choose no coins).
    # If this is not the first coin, add the number of ways for the previous coins.
    # If the coin is <= the target, add the number of ways of target - coin with the coin included.
    #
    # O(coins * amount) time.

    def change(self, amount: int, coins: List[int]) -> int:
        if len(coins) == 1:
            if amount % coins[0] == 0:
                return 1
            else:
                return 0

        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]
        for c in range(len(coins)):
            dp[c][0] = 1

        for c in range(len(coins)):
            for a in range(1, amount + 1):
                if coins[c] <= a:
                    dp[c][a] += dp[c][a - coins[c]]
                if c > 0:
                    dp[c][a] += dp[c - 1][a]
        
        return dp[-1][-1]
sol = Solution()
print(sol.change(5, [1,2,5]))
print(sol.change(3, [2]))
print(sol.change(10, [10]))
print(sol.change(100, [99, 1]))