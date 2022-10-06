class Solution:
    # Strip least significant bit using modulo and integer division by two.
    # Add to output in correct place by adding inverted bit multiplied by corresponding power of two.
    def findComplement(self, num: int) -> int:
        res = 0
        i = 0
        while num > 0:
            bit = num % 2
            num = (num - bit) // 2
            invertedBit = 0 if bit else 1
            res += (2 ** i) * invertedBit
            i += 1
        return res

sol = Solution()
print(sol.findComplement(num = 2))
print(sol.findComplement(num = 5))
print(sol.findComplement(num = 1))