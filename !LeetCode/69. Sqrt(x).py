from re import M


class Solution:
    # Binary search solution.
    # Find either the number that exactly squares to x, or 
    # find the first number that squares to something greater and
    # return that value minus 1.
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        l = 0
        r = x
        while l < r:
            m = (l + r) // 2
            p = m * m
            if p == x:
                return m
            elif p > x:
                r = m
            else:
                l = m + 1
        return l - 1 # Could also have been r - 1 since l == r at this point

sol = Solution()
print(sol.mySqrt(4))
print(sol.mySqrt(8))
print(sol.mySqrt(0))
print(sol.mySqrt(1))