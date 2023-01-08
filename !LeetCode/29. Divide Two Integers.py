class Solution:
    # Very similar to naive solution, but with an added optimization.
    # Instead of just repeatedly subtracting the same number, every
    # iteration add the number to itself and count up a multiplier.
    # The multipler is the corresponding number of subtractions of the
    # original divisor.
    # Since we add it to itself on every iteration, although the number corrsponds to
    # the divisor times the multiplier, we get it without doing multiplication.
    # When the number we are subtracting grows too large, reset to the
    # original divisor and start growing it again.
    # Since we double the size of the number we are subtracting on every iteration
    # this is O(logn) and fast enough to pass leetcode.
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2147483647
        MIN = -2147483648
        dividendNegative = dividend < 0
        divisorNegative = divisor < 0
        doNegate = dividendNegative != divisorNegative

        cnt = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            tmp = divisor  # Temporary number to subtract instead of divisor. tmp = divisor * multiplier.
            multiplier = 1  # Number of divisor subtractions done per iterations.
            while (
                dividend >= tmp
            ):  # Grow the tmp number until it is larger than the dividend and then reset tp multiplier of 1

                dividend -= tmp
                cnt += multiplier

                # Double size on every iteration:
                multiplier += multiplier
                tmp += tmp

        if doNegate:
            cnt = -cnt
        return max(MIN, min(MAX, cnt))

    # Naive solution.
    # Just count how many times you can subtract the divisor from the dividend.
    # The count is the floor division result.
    # We just need to check if one and only one of the inputs is negative,
    # and if so negate the results.
    # O(n) time and too slow to pass leetcode.
    def divideNaive(self, dividend: int, divisor: int) -> int:
        MAX = 2147483647
        MIN = -2147483648
        dividendNegative = dividend < 0
        divisorNegative = divisor < 0
        doNegate = dividendNegative != divisorNegative

        cnt = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            cnt += 1

        if doNegate:
            cnt = -cnt
        return max(MIN, min(MAX, cnt))


sol = Solution()
print(sol.divide(dividend=100, divisor=3))
print(sol.divide(dividend=10, divisor=3))
print(sol.divide(dividend=7, divisor=-3))
print("")
print(sol.divideNaive(dividend=100, divisor=3))
print(sol.divideNaive(dividend=10, divisor=3))
print(sol.divideNaive(dividend=7, divisor=-3))
