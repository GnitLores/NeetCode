class Solution:
    # Strip rightmost bit of each number using modulus and integer division method with base 2.
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x > 0 or y > 0:
            xDigit = x % 2
            yDigit = y % 2
            if xDigit != yDigit:
                res += 1
            x = (x - xDigit) // 2
            y = (y - yDigit) // 2

        return res

sol = Solution()
print(sol.hammingDistance(x = 1, y = 4))
print(sol.hammingDistance(x = 3, y = 1))
