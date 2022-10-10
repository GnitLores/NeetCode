class Solution:
    # Modulo / integer division method.
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        isNegative = num < 0
        num = abs(num)
        
        res = []
        while num > 0:
            digit = num % 7
            num = (num - digit) // 7
            res.append(str(digit))

        if isNegative:
            res.append("-")
            
        return "".join(res[::-1])

sol = Solution()
print(sol.convertToBase7(num = 100))
print(sol.convertToBase7(num = -7))