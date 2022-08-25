class Solution:
    # 2D dynamic programming solution.
    # If x chars from string 1 and y chars from string 2 have been added,
    # adding another char makes for a valid interleaving if 
    # x and y is a valid interleaving of the first x + y chars of string 3,
    # AND if char number x + y + 1 of string 3 is equal to the char being added.
    #
    # We add the subproblems to a table str1 x str2, and check if there was a valid interleaving
    # either to the left or above, and if the char is equal to the relevant char in string 3.
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        if len(s1) == 0:
            return True if s2 == s3 else False
        if len(s2) == 0:
            return True if s1 == s3 else False

        dp = [[False]*(len(s2) + 1) for i in range(len(s1) + 1)]
        dp[0][0] = True
        
        # Valid interleaving for str 1 with zero chars from str 2
        for i in range(0, len(s1)):
            if dp[i][0] == True and s1[i] == s3[i]:
                dp[i + 1][0] = True

        # Valid interleaving for str 2 with zero chars from str 1
        for k in range(0, len(s2)):
            if dp[0][k] == True and s2[k] == s3[k]:
                dp[0][k + 1] = True

        # Valid interleaving for every other number of included chars from both strings.
        for i in range(len(s1)):
            for k in range(len(s2)):

                if dp[i + 1][k] and s2[k] == s3[i + k + 1]:
                    dp[i + 1][k + 1] = True
                
                if dp[i][k + 1] and s1[i] == s3[i + k + 1]:
                    dp[i + 1][k + 1] = True

        return dp[-1][-1]

sol = Solution()
print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
print(sol.isInterleave("", "", ""))
print(sol.isInterleave("aabaac", "aadaaeaaf", "aadaaeaabaafaac"))