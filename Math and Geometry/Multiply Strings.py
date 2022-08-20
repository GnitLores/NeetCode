from typing import List


class Solution:
    # Solution using the ascii values of the characters to convert the strings to numbers,
    # multiply them and then convert the product back.
    # Unsure if this violates the rules. The conversion is done using math instead of with a function directly,
    # but the multiplication itself is normal.
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return 0

        def strToNum(s):
            # Iterate through the string backwards starting with ones.
            # Find the numerical value by ascii value relative to "0".
            # Multiply by digit's power of 10 (ones = 10^0, etc.).
            # Sum value of digits to get total number.
            num = sum([(ord(c) - ord("0")) * (10**i) for i, c in enumerate(s[::-1])])
            return num

        def numToStr(n):
            # Find least significant digit by mod 10 and shift number right by floored division by 10.
            # Convert to char by ascii value relative to "0".
            # Join to string.

            s = []
            while n > 0:
                d = n % 10
                s.append(chr(d + ord("0")))

                n = n // 10
            return "".join(s[::-1])

        return numToStr(strToNum(num1) * strToNum(num2))

    # Solution that uses a similar method to break the numbers down into the value of each digit.
    # e.g. "123" -> [3, 20, 100]
    # The product is the  calculated by multiplying all combinations of digit values and summing the result.
    # e.g. "123" * "10" = 3*10 + 20*10 + 100*10 + 3*0 + 20*0 + 100*0 = 1230
    # Should definitely follow the rules of the problem.
    def multiplyCombination(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return 0

        def strToDigits(s):
            num = [(ord(c) - ord("0")) * (10 ** i) for i, c in enumerate(s[::-1])]
            return num
        
        def numToStr(n):
            s = []
            while n > 0:
                d = n % 10
                s.append(chr(d + ord("0")))

                n = n // 10
            return "".join(s[::-1])

        num1 = strToDigits(num1)
        num2 = strToDigits(num2)

        product = 0
        for n1 in num1:
            for n2 in num2:
                product += n1 * n2

        return numToStr(product)

sol = Solution()
print(sol.multiply("123", "45"))
print(sol.multiply("2", "3"))
print(sol.multiply("123", "456"))
print(sol.multiply("123", "0"))
print("")
print(sol.multiplyCombination("123", "45"))
print(sol.multiplyCombination("2", "3"))
print(sol.multiplyCombination("123", "456"))
print(sol.multiplyCombination("123", "0"))