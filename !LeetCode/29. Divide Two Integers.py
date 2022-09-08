class Solution:
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
        doNegate = True if dividendNegative != divisorNegative else False

        cnt = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            cnt += 1

        if doNegate: cnt = -cnt
        return max(MIN, min(MAX, cnt))

sol = Solution()
print(sol.divideNaive(dividend = 100, divisor = 3))
print(sol.divideNaive(dividend = 10, divisor = 3))
print(sol.divideNaive(dividend = 7, divisor = -3))