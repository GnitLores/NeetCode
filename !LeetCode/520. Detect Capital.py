class Solution:
    # Check if word is equal to itself with all letters in uppercase or lower case.
    # A single letter word is always valid.
    # Multiple letter words are valid if all letters except the first are equal
    # to the same letters in lower case.
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1: return True
        if word == word.upper(): return True
        allLower = word.lower()
        if word == allLower: return True
        if word[1:] == allLower[1:]: return True

        return False

sol = Solution()
print(sol.detectCapitalUse(word = "USA"))
print(sol.detectCapitalUse(word = "FlaG"))
print(sol.detectCapitalUse(word = "Flag"))
print(sol.detectCapitalUse(word = "a"))
print(sol.detectCapitalUse(word = "thrhrta"))