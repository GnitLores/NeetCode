class Solution:
    # The biggest issue (besides all the edge case inputs) is preventing the number from overflowing.
    # In python it is actually very easy to do because integers are arbitrarily large, but assuming that
    # the system only allows 32 bit integers makes it more difficult.
    # We check if the intermediate result exeeds the max or min without the next last before adding the next digit.
    # We also check if it is equal to it AND the last digits are equal.
    # This can actually fail on an edge case like "-2147483649" because python rounds towards infinity on modulus and
    # integer division and not towards zero like other languages.
    def myAtoi(self, s: str) -> int:

        MAX = 2147483647
        MIN = -2147483648

        res = 0
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i >= len(s):
            return res
        if s[i] != "-" and s[i] != "+" and not "0" <= s[i] <= "9":
            return res

        signFound = False
        isPositive = True
        if s[i] == "-":
            isPositive = False
            signFound = True
            i += 1

        elif s[i] == "+":
            signFound = True
            i += 1

        if i >= len(s):
            return res
        if signFound and not "0" <= s[i] <= "9":
            return res

        while i < len(s) and "0" <= s[i] <= "9":
            digit = int(s[i]) if isPositive else -int(s[i])
            # if res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10):
            #     return MAX
            # if res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10):
            #     return MIN
            res = (res * 10) + digit
            if res < MIN:
                return MIN
            if res > MAX:
                return MAX
            i += 1
        return res


sol = Solution()
print(sol.myAtoi(s="-2147483649"))
print(sol.myAtoi(s="-+1"))
print(sol.myAtoi(s="+1"))
print(sol.myAtoi(s="-91283472332"))
print(sol.myAtoi(s="42"))
print(sol.myAtoi(s="   -42"))
print(sol.myAtoi(s="4193 with words"))
print(sol.myAtoi(s="41.93 with words"))
print(sol.myAtoi(s=".4193 with words"))
print(sol.myAtoi(s="with words 4193"))
