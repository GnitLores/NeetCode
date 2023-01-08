class Solution:
    # Solve by reversing the number.
    # Find the least significant digit with mod 10, and
    # strip it with integer division by 10.
    # Add it to the reverse number and multiply by 10 for every
    # digit to get the least significant digit at the most significant
    # place.
    def isPalindromeReverseDigits(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        originalNum = x
        reverseNum = 0
        while x > 0:
            reverseNum *= 10
            reverseNum += x % 10
            x //= 10
        return originalNum == reverseNum

    # Just cast to string, reverse and check.
    def isPalindromeReverseString(self, x: int) -> bool:
        if x < 0:
            return False
        return True if x < 10 else str(x) == str(x)[::-1]

    # Cast to string and check with two pointers.
    def isPalindromeString(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        x = str(x)
        return self.checkPalindrom(x)

    # Strip least significant digit and add to list.
    # Check list with two pointers.
    def isPalindromeDigits(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10

        return self.checkPalindrom(digits)

    def checkPalindrom(self, digits):
        l, r = 0, len(digits) - 1
        while l < r:
            if digits[l] != digits[r]:
                return False
            l += 1
            r -= 1
        return True


sol = Solution()
print(sol.isPalindromeReverseDigits(121))
print(sol.isPalindromeReverseDigits(-121))
print(sol.isPalindromeReverseDigits(10))
print("")
print(sol.isPalindromeReverseString(121))
print(sol.isPalindromeReverseString(-121))
print(sol.isPalindromeReverseString(10))
print("")
print(sol.isPalindromeString(121))
print(sol.isPalindromeString(-121))
print(sol.isPalindromeString(10))
print("")
print(sol.isPalindromeDigits(121))
print(sol.isPalindromeDigits(-121))
print(sol.isPalindromeDigits(10))
