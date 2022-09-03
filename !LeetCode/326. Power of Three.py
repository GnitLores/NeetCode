class Solution:
    # 3^0 is 1
    # 3^1 is 3
    # If x is a negative number, n would be a fraction of 1, not an integer.
    # Thus, for n to be a power of 3, n must be either 1 or an integer >= 3
    # that becomes 1 through successively dividing by 3.
    # Using modulo is not enough because it returns zero if n is divisible by 3,
    # but that's not the same as the number being a power of three.
    # O(log_3(n))
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        if n < 3: return False
        while n >= 3:
            n /= 3
        if n == 1: return True
        return False

sol = Solution()
print(sol.isPowerOfThree(45))
print(sol.isPowerOfThree(27))
print(sol.isPowerOfThree(0))
print(sol.isPowerOfThree(-1))