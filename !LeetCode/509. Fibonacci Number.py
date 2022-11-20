class Solution:
    # Dynamic programming solution.
    # Store only two previous values and calculate iteratively.
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        first, second = 1, 0
        i = 1
        while i < n:
            tmp = first + second
            second = first
            first = tmp
            i += 1
        return first

sol = Solution()
print(sol.fib(n = 4))