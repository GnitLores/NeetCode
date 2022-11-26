class Solution:
    # Solution using the modulo and integer division to strip
    # least significant bits and mulitplications by powers to sum
    # up the flipped bits.
    # In principle, XORing with all 1s should flip all bits,
    # but the way python represents integers makes this more tricky.
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        res = 0
        i = 0
        while n > 0:
            bit = not (n % 2)
            n //= 2
            res += bit * (2 ** i)
            i = i + 1
        return res

sol = Solution()
print(sol.bitwiseComplement(n = 5))
print(sol.bitwiseComplement(n = 7))
print(sol.bitwiseComplement(n = 10))