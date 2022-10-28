from typing import List


class Solution:
    # Strip digits with modulo and integer division method.
    # Check if number is not divisible by digit or digit is zero.
    # O(n logn) time.
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isValid(n):
            tmp = n
            while tmp > 0:
                digit = tmp % 10
                if digit == 0 or n % digit != 0: return False
                tmp = tmp // 10
            return True

        return [n for n in range(left, right + 1) if isValid(n)]

sol = Solution()
print(sol.selfDividingNumbers(left = 1, right = 22))
print(sol.selfDividingNumbers(left = 47, right = 85))