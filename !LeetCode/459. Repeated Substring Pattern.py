class Solution:
    # We know that the substring must start from the first character
    # and be of a length that the full string is divisible by.
    # We also know that if the string is even length, the greatest possible
    # substring is half that length.
    # If it is uneven length, the greatest possible substring is one third that length
    # (actually it depends on the number, i.e. for 25 the greatest possible substring
    # would be a fifth that length but that would be a minor optimization).
    #
    # Try substrings up to the max length and see if duplicating them results in the
    # full string.
    def repeatedSubstringPattern(self, s: str) -> bool:
        w = len(s)
        if w < 2: return False
        maxLen = w // 2 if w % 2 == 0 else w // 3

        for sw in range(1, maxLen + 1):
            if w % sw == 0:
                substr = s[0:sw]
                if s == substr * (w // sw):
                    return True
                
        return False

sol = Solution()
print(sol.repeatedSubstringPattern(s = "abab"))
print(sol.repeatedSubstringPattern(s = "aba"))
print(sol.repeatedSubstringPattern(s = "abcabcabcabc"))
print(sol.repeatedSubstringPattern(s = "abcabcabcabcabc"))