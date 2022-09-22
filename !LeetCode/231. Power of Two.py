class Solution:
    # 2^0 is 1
    # 2^1 is 2
    # If x is a negative number, n would be a fraction of 1, not an integer.
    # Thus, for n to be a power of 2, n must be either 1 or an integer >= 2
    # that becomes 1 through successively dividing by 2.
    # Using modulo is not enough because it returns zero if n is divisible by 2,
    # but that's not the same as the number being a power of two.
    # O(logn)
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True
        if n < 2: return False
        while n >= 2:
            n /= 2
        if n == 1: return True
        return False

sol = Solution()
print(sol.isPowerOfTwo(n = 1))
print(sol.isPowerOfTwo(n = 16))
print(sol.isPowerOfTwo(n = 3))