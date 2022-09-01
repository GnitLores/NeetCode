class Solution:
    # 2-D dynamic programming solution.
    # Suppose that we add a letter to the string we are searching in.
    # If that letter does not match the last letter of the string we are searching for,
    # it does not change the number of possible substrings.
    # If it does match, then the number of substrings is the number we had before adding it,
    # plus the number of substrings when excluding the last letter of both strings.
    # This is because the new last letter becomes a valid final letter of all of those substrings.
    # Thus the recursion relation is:
    # substrings(s, t):
    #   if s[-1] == t[-1]:
    #       substrings = substrings(s_(n-1), t) + substrings(s_(n-1), t_(n-1))
    #   else:
    #       substrings = substrings(s_(n-1), t)
    #
    # This solution uses a 2D array to calculate this iteratively.
    # The entire left column is ones because there is one way to find an empty string in any string (no letters).
    # O(s * t) time.
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for r in range(len(s) + 1):
            dp[r][0] = 1

        for r in range(1, len(s) + 1):
            for c in range(1, len(t) + 1):
                if s[r - 1] == t[c - 1]:
                    dp[r][c] =  dp[r - 1][c] + dp[r - 1][c - 1] 
                else:
                    dp[r][c] =  dp[r - 1][c]
        return dp[-1][-1]

sol = Solution()
print(sol.numDistinct(s = "rabbbit", t = "rabbit"))
print(sol.numDistinct(s = "babgbag", t = "bag"))