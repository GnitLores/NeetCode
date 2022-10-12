class Solution:
    # This is kind of a trick questions.
    # The longest subsequence of a string is the string itself.
    # If the strings are not of equal length, the shorter string cannot possibly
    # contain the longer string.
    # If they are of equal length, the only way one can contain the other is if the
    # strings are identical.
    # Thus the answer is always the length of the longer string unless the strings are identical.
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b: return -1
        return max(len(a), len(b))

sol = Solution()
print(sol.findLUSlength(a = "abc", b = "aebdc"))
print(sol.findLUSlength(a = "aba", b = "cdc"))
print(sol.findLUSlength(a = "aaa", b = "bbb"))
print(sol.findLUSlength(a = "aaa", b = "aaa"))