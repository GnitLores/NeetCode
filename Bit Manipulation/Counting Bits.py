class Solution(object):
    # A solution similar to Number of 1 Bits could be used (modulus 2 and right shifting).
    # However, as n grows, the number of times a number can be divided by two grows by O(logn).
    # Doing this for each integer would give a total complexity of O(nlogn) time.
    #
    # Instead, observing the bit representation makes a pattern clear.
    # n:
    # 0   [0 0 0 0] = 0
    # 1   [0 0 0 1] = 1 + dp[n-1]
    # 2   [0 0 1 0] = 1 + dp[n-2]
    # 3   [0 0 1 1] = 1 + dp[n-2]
    # 4   [0 1 0 0] = 1 + dp[n-4]
    # 5   [0 1 0 1] = 1 + dp[n-4]
    # 6   [0 1 1 0] = 1 + dp[n-4]
    # 7   [0 1 1 1] = 1 + dp[n-4]
    # 8   [1 0 0 0] = 1 + dp[n-8]
    # ...
    #
    # It can be solved as a dynamic programming problem in O(n) time.
    def countBits(self, n):
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i == offset * 2:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

sol = Solution()
print(sol.countBits(2))
print(sol.countBits(5))


