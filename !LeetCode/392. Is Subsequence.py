class Solution:
    # Iterate through main string, Keeping pointer to
    # char in substring and increment
    # pointer whwn char is found.
    # Return True when all chars are found.
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        k = 0
        for c in t:
            if s[k] == c:
                k += 1
                if k == len(s):
                    return True
        return False

sol = Solution()
print(sol.isSubsequence(s = "abc", t = "ahbgdc"))
print(sol.isSubsequence(s = "axc", t = "ahbgdc"))
