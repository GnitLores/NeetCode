class Solution:
    # Two pointer solution.
    # Turn to list of chars, search for letters from both sides and reverse positions
    # until pointers meet. Join output as string.
    def reverseOnlyLetters(self, s: str) -> str:
        s = [c for c in s]
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalpha(): l += 1
            while l < r and not s[r].isalpha(): r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)

sol = Solution()
print(sol.reverseOnlyLetters(s = "ab-cd"))
print(sol.reverseOnlyLetters(s = "a-bC-dEf-ghIj"))
print(sol.reverseOnlyLetters(s = "Test1ng-Leet=code-Q!"))