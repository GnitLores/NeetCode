class Solution:
    # Logarithmic time solution, making use of the fact that:
    # a^n * a^m = a^(a + m)
    # and also that:
    # a^n * b^n = (a*b)^n
    #
    # So x^n = x^(n/2) * x^(n/2) = (x*x)^(n/2)
    #
    # With even n this is easy to calculate, and with odd n we can use floor division like this:
    # x^n = x^(n//2) * x^(n//2) * x
    # Since we halve n every time, the number of iterations grows logarithmically.
    # O(logn) time.
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2) * x

    # Naive solution just multiplying x by itself in a loop.
    # O(n) time.
    def myPowNaive(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        for _ in range(n):
            res = res * x
        return res

sol = Solution()
print(sol.myPow(2.00000, 10))
print(sol.myPow(2.10000, 3))
print(sol.myPow(2.00000, -2))
print("")
print(sol.myPowNaive(2.00000, 10))
print(sol.myPowNaive(2.10000, 3))
print(sol.myPowNaive(2.00000, -2))