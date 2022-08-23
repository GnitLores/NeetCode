class Solution:
    # Re using the solution from Longest Palindromic Substring problem.
    # Check each char as center of odd palindrom and together with next char as center of even palindrome.
    # Let palindromes grow from center until not a palindrome anymore.
    # O(n^2) time.
    def countSubstrings(self, s: str) -> int:
        res = [0]

        def checkPalindromeCenter(i, isOdd):
            l = i # Left side of palindrome
            r = i if isOdd else i + 1 # Right, for odd point same char as l, for even point next char.
            while l >= 0 and r < len(s) and s[l] == s[r]: # If pointers are within limits and this is still a palindrome
                res[0] += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            checkPalindromeCenter(i, True) # Find odd palindromes with i as center
            checkPalindromeCenter(i, False) # Find even palindromes with i as center

        return res[0]

sol = Solution()
print(sol.countSubstrings("abc"))
print(sol.countSubstrings("aaa"))
print(sol.countSubstrings("meuuopoinrgeuhamahubywdvaidoodpbfe")) # uu uhamahu dood