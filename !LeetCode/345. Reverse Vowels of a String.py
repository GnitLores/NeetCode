class Solution:
    # Two pointer solution
    # Search for vowels on boths sides and then swap them.
    # Stop when pointers meet.
    # O(n) time.
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s = [c for c in s]
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
                
        return "".join(s)

sol = Solution()
print(sol.reverseVowels("hello"))
print(sol.reverseVowels("leetcode"))