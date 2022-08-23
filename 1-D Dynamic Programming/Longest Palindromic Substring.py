class Solution:
    # Not a dynamic programming solution.
    # A palindrome can become longer if the next char to the right and left of it are identical.
    # Checking if something is a palindrome is O(n), and there are O(n^2) substrings, so brute force would be O(n^3).
    # Instead, we let every char be the center of a palindrome and see how large it can get by adding character left and right.
    # The only complication is that palindromes with an even number of chars do not have a center, but instead two identical chars as center.
    # O(n^2) time.
    def longestPalindrome(self, s: str) -> str:
        res = [""]
        length = [0]

        def checkPalindromeCenter(i, isOdd):
            l = i # Left side of palindrome
            r = i if isOdd else i + 1 # Right, for odd point to same char as l, for even point to next char.
            longerFound = False
            while l >= 0 and r < len(s) and s[l] == s[r]: # If pointers are within limits and this is still a palindrome
                if (r - l + 1) > length[0]: # And it is the longest palindrome so far
                    length[0] = (r - l + 1)
                    longerFound = True
                    lPal = l
                    rPal = r
                l -= 1
                r += 1
            if longerFound: res[0] = s[lPal: rPal + 1] # It is important to only store the palindrome outside of the loop, since it is an O(n) operation to create the string.

        for i in range(len(s)):
            checkPalindromeCenter(i, True) # Find odd palindromes with i as center
            checkPalindromeCenter(i, False) # Find even palindromes with i as center

        return res[0]
        
sol = Solution()
print(sol.longestPalindrome("meuuopoinrgeuhamahubywdvaidoodpbfe")) # uu uhamahu dood
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))