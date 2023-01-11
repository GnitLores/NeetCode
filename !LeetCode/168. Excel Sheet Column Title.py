class Solution:
    # The main complication is that the excel number system is different
    # from a normal base 26 number system in that A maps to 1 and not 0.
    # To accommodate for this we need to subtract by 1 when finding the digit.
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            digit = (columnNumber - 1) % 26
            columnNumber = (columnNumber - digit) // 26
            res.append(chr(ord("A") + digit))

        return "".join(reversed(res))


sol = Solution()
print(sol.convertToTitle(columnNumber=1))
print(sol.convertToTitle(columnNumber=28))
print(sol.convertToTitle(columnNumber=701))
