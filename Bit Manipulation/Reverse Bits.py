class Solution:
    # Solution using bitshifts and modulus.
    # If the rightmost bit of n is 1, add 1 to rightmost position of k and shift left. Shift n right.
    # O(1) time as there are always 32 bits.
    def reverseBits(self, n):
        k = 0
        for _ in range(0, 32):
            k = k << 1
            k += n % 2
            n = n >> 1
        return k


sol = Solution()
print(sol.reverseBits(5))
print(sol.reverseBits(43261596))
print(sol.reverseBits(4294967293))
