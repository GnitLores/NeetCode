class Solution:
    # Get value of chars by ascii value relative to "A".
    # This is a base 26 system, so find value by multiplying digits
    # by powers of 26 and calculating the sum.
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        res = 0
        for i, c in enumerate(columnTitle):
            res += (ord(c) - ord("A") + 1) * (26 ** i)
        return res

sol = Solution()
print(sol.titleToNumber("A"))
print(sol.titleToNumber("AB"))
print(sol.titleToNumber("ZY"))