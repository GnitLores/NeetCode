class Solution:
    # Remove dashes and convert to upper case.
    # Find length of first group with modulo, add it to array,
    # and then add all k size groups remaining.
    # Join array of strings on dash.
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
        s = s.upper()

        first = len(s) % k
        if first == 0: first = k
        res = [s[0:first]]
        
        l = first
        r = l + k
        while r <= len(s):
            res.append(s[l:r])
            l += k
            r += k

        return "-".join(res)

sol = Solution()
print(sol.licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4))
print(sol.licenseKeyFormatting(s = "2-5g-3-J", k = 2))