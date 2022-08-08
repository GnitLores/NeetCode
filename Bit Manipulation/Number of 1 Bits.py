class Solution(object):
    # Solution using modulus operation and rightwise bitshift.
    # If the lowest bit is one, the number is odd and mod 2 = 1.
    # Bitshift moves the next bit to the lowest bit position.
    # O(1) because there are always e.g. 32 bits.
    def hammingWeight(self, n):
        ones = 0
        while n > 0:
            ones += n % 2
            n = n >> 1
        return ones

sol = Solution()
print(sol.hammingWeight(11))