class Solution:
    # The factors of a negative integer cannot possibly be limited to 2, 3, and 5, so always false.
    # 0 has an infinite number of factors so always false.
    # 1 has no prime factors other than 2, 3, and 5 (and not those either) so always true.
    # Prime factorization is unique, so there exists a unique combination of primes that multiply to any positive integer.
    # We can just repeatedly check if the number is divisible by 2, 3 and 5 and divide if it is.
    # If we come to a number that is not, then it is not an ugly number, and multiplying it by 2, 3 or 5 won't make it one.
    # Thus the original number was not ugly.
    # If it was ugly we would inevitably arrive at 1.
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False

        def reduceFactor(n, p):
            while n % p == 0:
                n //= p
            return n

        n = reduceFactor(n, 2)
        n = reduceFactor(n, 3)
        n = reduceFactor(n, 5)
        return n == 1


sol = Solution()
print(sol.isUgly(n=6))
print(sol.isUgly(n=1))
print(sol.isUgly(n=14))
