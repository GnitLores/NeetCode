class Solution:
    # Memoized iterative solution using same principle as fibonacchi sequence method.
    # Track three prior values and calculate next tribonacchi number.
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        first, second, third = 1, 1, 0
        i = 2
        while i < n:
            tmp = first + second + third
            third = second
            second = first
            first = tmp
            i += 1
        return first

sol = Solution()
print(sol.tribonacci(n = 4))
print(sol.tribonacci(n = 25))