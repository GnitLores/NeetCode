class Solution:
    # This problem would be easier to solve by just converting the numbers
    # digit by digit to chars using ASCII value, recreating the numbers
    # as int using powers of ten and then doing integer addition.
    # However, this doesn't seem to follow the spirit of the problem.
    # It also want big integer addition without using big int, and while
    # this would be no problem in python, it would not work in other languages
    # without overflow.
    #
    # Instead, we will just work on the strings and only add digit by digit,
    # making sure to carry when getting digits over 9.
    # Finally we can just join the list of resulting digit chars to a string.
    def addStrings(self, num1: str, num2: str) -> str:
        # Zero pad the numbers to be the same length and reverse the order to
        # make them easier to work with.
        maxLen = max(len(num1), len(num2))
        if len(num1) < maxLen: num1 = num1.zfill(maxLen)
        if len(num2) < maxLen: num2 = num2.zfill(maxLen)
        num1 = num1[::-1]
        num2 = num2[::-1]

        doCarry = False
        res = []
        for c1, c2 in zip(num1, num2):
            digit = ord(c1) + ord(c2) - 2 * ord("0") # Addition of single digit using ASCII values

            if doCarry:
                digit += 1

            if digit > 9:
                digit -= 10
                doCarry = True
            else:
                doCarry = False
            
            res.append(chr(digit + ord("0")))

        if doCarry:
            res.append("1")

        return "".join(res[::-1])

sol = Solution()
print(sol.addStrings(num1 = "11", num2 = "123"))
print(sol.addStrings(num1 = "456", num2 = "77"))
print(sol.addStrings(num1 = "0", num2 = "0"))