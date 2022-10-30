class Solution:
    # The max right value is 10^6, which means that the potential number of
    # bits is very limited.
    # We can just create a set of all the prime numbers up to that number
    # and for each word convert it to binary string representation, count
    # the number of ones and check if it is in the set of primes.
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
        res = 0
        for n in range(left, right + 1):
            if bin(n).count("1") in primes:
                res += 1
        return res

sol = Solution()
print(sol.countPrimeSetBits(left = 6, right = 10))
print(sol.countPrimeSetBits(left = 10, right = 15))