class Solution:
    # Reverse string, strip leading whitespace.
    # Index of first space corresponds to length of first word in reversed string.
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s[::-1].strip()
        if not s:
            return 0

        i = 0
        while i < len(s) and s[i] != " ":
            i += 1
        return i


sol = Solution()
print(sol.lengthOfLastWord(s=""))
print(sol.lengthOfLastWord(s="    "))
print(sol.lengthOfLastWord(s="Hello World"))
print(sol.lengthOfLastWord(s="   fly me   to   the moon  "))
print(sol.lengthOfLastWord(s="luffy is still joyboy"))
