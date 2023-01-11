class Solution:
    # Clever bit manipulation solution from leetcode:
    #
    # 2->0000 0001 <-
    # 2->0000 0010 <-
    # 3->0000 0011
    # 4->0000 0100 <-
    # 5->0000 0101
    # 6->0000 0110
    # 7->0000 0111
    # 8->0000 1000 <-
    #
    # Powers of two all have leading 1 bit followed by zeroes
    # Consequently, ANDing that number by the number -1 gives 0:
    # bit representation of 7  -> 0111
    # bit representation of 8  -> 1000
    # bitwise AND of 7 and 8 -> 0000
    #
    # O(1) in principle but it actually seems to run slower than my own solution
    # for the leetcode test cases.
    def isPowerOfTwoBitwise(self, n: int) -> bool:
        if n == 1:
            return True
        return False if n < 2 else n & (n - 1) == 0

    # 2^0 is 1
    # 2^1 is 2
    # If x is a negative number, n would be a fraction of 1, not an integer.
    # Thus, for n to be a power of 2, n must be either 1 or an integer >= 2
    # that becomes 1 through successively dividing by 2.
    # Using modulo is not enough because it returns zero if n is divisible by 2,
    # but that's not the same as the number being a power of two.
    # O(logn)
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 2:
            return False
        while n >= 2:
            n /= 2
        return n == 1


sol = Solution()
print(sol.isPowerOfTwoBitwise(n=1))
print(sol.isPowerOfTwoBitwise(n=16))
print(sol.isPowerOfTwoBitwise(n=3))
print("")
print(sol.isPowerOfTwo(n=1))
print(sol.isPowerOfTwo(n=16))
print(sol.isPowerOfTwo(n=3))
