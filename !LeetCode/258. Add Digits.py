class Solution:
    def addDigits(self, num: int) -> int:
        # iteratively split split off least significant digit with mod and integer division by 10.
        # Do it in rounds as long as the number is greater than 10.
        def addRound(num):
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res

        while num >= 10:
            num = addRound(num)
        return num

    # Clever solution from leetcode.
    # If you write out the sum for increasing numbers, it becomes apparent that
    # the sum = (number % 9) unless the result is 0 in which case it becomes 9.
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        num %= 9
        if num == 0:
            num = 9
        return num


sol = Solution()
print(sol.addDigits(num=38))
print(sol.addDigits(num=0))
print("")
print(sol.addDigits(num=38))
print(sol.addDigits(num=0))
