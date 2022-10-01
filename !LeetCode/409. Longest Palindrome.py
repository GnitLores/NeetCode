class Solution:
    # A palindrome is consists of pairs of matching characters,
    # so count pairs using set and increment by 2 for each pair.
    # In addition, there can be at most a single character in the middle
    # without a matching character.
    # O(n) time.
    def longestPalindrome(self, s: str) -> int:
        hashset = set()
        res = 0
        for c in s:
            if c in hashset:
                hashset.remove(c)
                res += 2
            else:
                hashset.add(c)

        if len(hashset) > 0:
            res += 1
        return res

sol = Solution()
print(sol.longestPalindrome(s = "abccccdd"))
print(sol.longestPalindrome(s = "a"))
