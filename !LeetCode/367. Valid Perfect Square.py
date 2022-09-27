class Solution:
    # Binary search solution.
    # O(log num) time.
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            m = l + (r - l) // 2
            sq = m * m
            if sq > num:
                r = m - 1
            elif sq < num:
                l = m + 1
            elif sq == num:
                return True
        return False

sol = Solution()
print(sol.isPerfectSquare(16))
print(sol.isPerfectSquare(14))