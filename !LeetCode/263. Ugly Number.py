class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1: return True
        if n < 1: return False
        
        def reduceFactor(n, p):
            while n % p == 0:
                n = n // p
            return n
        
        n = reduceFactor(n, 2)
        n = reduceFactor(n, 3)
        n = reduceFactor(n, 5)
        return n == 1

sol = Solution()
print(sol.isUgly(n = 6))
print(sol.isUgly(n = 1))
print(sol.isUgly(n = 14))