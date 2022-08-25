class Solution:
    # 2-D dynamic programming solution.
    # If the first char of two strings A and B match, then the LCS is 1 + the LCS of the rest of both strings without the first char.
    # If they don't match, then the LCS is the max of the LCS between all of A and the rest of B and all of B and the rest of A.
    # This way the problem can be broken down into subproblems.
    # Example:
    # LCS("abc", "ace") = 1 + LCS("bc", "ce")
    # LCS("abc", "bce") = max(LCS("bc", "bce"), LCS("abc", "ce"))
    #
    # We create a grid indicating the LCS of the rest of the string starting from the char in that row and column.
    # We initialize an additional column and row of zeros to the right and bottom to indicate empty strings.
    # We can then calculate the problems backwards only matching single chars.
    # If there is a match, the LCS is the LCS diagonally right and down + 1.
    # If there is not a match, the LCS is the max of LCS down and LCS right.
    #
    # O(m * n) time.
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        for i in range(len(text1) + 1):
            dp.append([0]*(len(text2) + 1))

        cnt = 0
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])  
                
        return dp[0][0]

sol = Solution()
print(sol.longestCommonSubsequence("abcde", "ace"))
print(sol.longestCommonSubsequence("abc", "abc"))
print(sol.longestCommonSubsequence("abc", "def"))