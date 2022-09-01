class Solution:
    # 2D dynamic programming solution.
    # Suppose that we include another letter to one of the strings.
    # There are four options for dealing with it:
    # 1 - If the last characters of the two strings match, then the min number of operations
    # is the the same as for the two strings both with their last char removed. We don't need
    # to add a command.
    # Otherwise, if they don't match we must use a command:
    # 2 - We can replace the character with the matching character, which is the same as before,
    # but now we used a command. Ex: "h" and "r" becomes "r" and "r" -> same as "" and "" as per case 1.
    # 3 - We can insert the matching character, which results in case 1 but with one character more
    # in the string and a command used. Ex: "h" and "r" becomes "rh" and "r" same as "" and "h" as per case 1.
    # 4 - We can delete the character, which results which results in the same problem but with
    # the string once char shorter. Ex: "h" and "r" becomes "" and "r".
    # We make a 2D matrix indicating the characters included from each string (rows = characters of start
    # string, cols = characters of end string). The top row and left column indicate the empty strings:
    # If two characters match, the min number is the min number up and to the left.
    # If they don't match, the min number of commands is 1 + min(up and left (replace), up (remove), and left (insert))
    # The top row and left column are initialized to 0:1:len(string) because it would take that number of insertions/removals to reach the target.
    # O(s1 * s2) time.

    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for r in range(len(word1) + 1):
            dp[r][0] = r
        for c in range(len(word2) + 1):
            dp[0][c] = c

        for r in range(1, len(word1) + 1):
            for c in range(1, len(word2) + 1):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])

        return dp[-1][-1]

sol = Solution()
print(sol.minDistance(word1 = "horse", word2 = "ros"))
print(sol.minDistance(word1 = "intention", word2 = "execution"))