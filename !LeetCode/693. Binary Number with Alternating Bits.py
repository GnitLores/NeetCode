class Solution:
    # Strip rightmost bit using modulo and integer division method for base 2.
    # Check if rightmost digit is ever the same twice in a row.
    # O(logn) time.
    def hasAlternatingBits(self, n: int) -> bool:
        bitState = None
        while n > 0:
            digit = n % 2
            n = n // 2

            if bitState == None:
                bitState = digit
                continue
            if digit == bitState:
                return False
            bitState = digit
            
        return True

sol = Solution()
print(sol.hasAlternatingBits(n = 5))
print(sol.hasAlternatingBits(n = 7))
print(sol.hasAlternatingBits(n = 11))