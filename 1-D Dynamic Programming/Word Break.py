from typing import List


class Solution:
    # Dynamic programming solution.
    # For each character record if it was possible to break it there.
    # For each word, check if the lest part of the subtring matches the word,
    # and if it was possible to break the string befor that substring.
    # O(n*words*wordlength) time complexity, but these are all capped -
    # escpecially wordlength which is capped to 20.
    # Can probably be considered O(n*words) time.
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for w in wordDict:
                wStart = i - len(w) + 1
                if wStart >= 0:
                    if dp[wStart] == True and s[wStart:i + 1] == w:
                        dp[i + 1] = True

        return dp[-1]

sol = Solution()
print(sol.wordBreak("leetcode", ["leet","code"]))
print(sol.wordBreak("applepenapple",  ["apple","pen"]))
print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))