class Solution:
    # Flip between reverse and no reverse state while
    # iterating through the string in chunks of k characters
    # adding to the output.
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        l = 0
        doReverse = True
        while l < len(s):
            r = min(l + k, len(s))
            res.append(s[l:r][::-1]) if doReverse else res.append(s[l:r])
            doReverse = not doReverse
            l = r

        return "".join(res)

sol = Solution()
print(sol.reverseStr(s = "abcdefg", k = 2))
print(sol.reverseStr(s = "abcd", k = 2))