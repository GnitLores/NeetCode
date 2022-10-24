class Solution:
    # Two pointer solution.
    # We want to avoid trying to remove all characters because that
    # would make this an O(n^2) problem.
    # If we do a normal two pointer solution allowing one character
    # to be skipped, we run into the problem that locally it appears
    # both the left and right character can be skipped (because the
    # next character will be locally valid on both sides).
    # However, we can't know if either of them can be removed to
    # result in a valid palindrome without verifying for the remainder
    # of the string.
    # We can solve this with a helper function that checks if a string
    # is a palindrom and returns the left and right indices at which
    # the check fails.
    # We can then check the full string, and if it is not a palindrome,
    # check the subtring starting and ending at those indices twice,
    # each time with a character removed from either end.
    #
    # O(n) because we process the array at most twice asonly one skip is possible.
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            if len(s) == 1: return True, 0, 0
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False, l, r
            return True, l, r

        isValid, l, r = isPalindrome(s)
        if isValid: return True 
        isValid, _, _ = isPalindrome(s[l:r]) # Shift r
        if isValid: return True
        isValid, _, _ = isPalindrome(s[l + 1:r + 1]) # Shift l
        if isValid: return True
        return False



sol = Solution()
print(sol.validPalindrome(s = "aba"))
print(sol.validPalindrome(s = "abca"))
print(sol.validPalindrome(s = "abc"))
print(sol.validPalindrome(s = "ebcbbececabbacecbbcbe"))