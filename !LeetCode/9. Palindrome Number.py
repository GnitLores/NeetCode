class Solution:
    # Strip least significant digit and add to list.
    # Check list with two pointers.
    def isPalindromeDigits(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True

        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10

        l, r = 0, len(digits) - 1
        while l < r:
            if digits[l] != digits[r]:
                return False
            l += 1
            r -= 1
        return True

sol = Solution()
print(sol.isPalindromeDigits(121))
print(sol.isPalindromeDigits(-121))
print(sol.isPalindromeDigits(10))