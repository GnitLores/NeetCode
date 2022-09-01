class Solution:
    
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