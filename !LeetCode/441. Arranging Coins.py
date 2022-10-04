class Solution:
    # Binary search solution from leetcode using sum of series formula.
    # O(logn)
    def arrangeCoins(self, n: int) -> int:
        l, r, ans = 1, n, 0
        while l <= r:
            rows = (l + r) >> 1
            coinsNeeded = rows * (rows + 1) >> 1
            if coinsNeeded <= n:
                l, ans = rows + 1, rows
            else:
                r = rows - 1
        return ans

    # Brute force solution.
    # O(sqrt n)
    def arrangeCoinsBruteForce(self, n: int) -> int:
        i = 0
        while n > 0:
            i += 1
            n -= i
            
        if n == 0:
            return i
        else:
            return i - 1

sol = Solution()
print(sol.arrangeCoins(5))
print(sol.arrangeCoins(8))
print(sol.arrangeCoins(1))
print(sol.arrangeCoins(6))
print("")
print(sol.arrangeCoinsBruteForce(5))
print(sol.arrangeCoinsBruteForce(8))
print(sol.arrangeCoinsBruteForce(1))
print(sol.arrangeCoinsBruteForce(6))