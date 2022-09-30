class Solution:
    # The main challenge is dealing with negative numbers.
    # With two's complement, -1 is stored as the largest possible
    # representation (-1 => ffffffff = 4294967295) and greater negative
    # numbers decrement from there (-2 => fffffffe = 4294967294).
    # That means that we can just add the negative number to 4294967294
    # (amd add 1 since negative numbers start at -1) and then convert that
    # number to hex instead.
    # The hex conversion is the usual modulo and binary division method with
    # the added necessity of mapping numbers greater than 9 to letters.
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        if num < 0:
            negMax = 4294967295
            num = negMax + num + 1

        chars = ["a", "b", "c", "d", "e", "f"]
        hex = []
        while num > 0:
            digit = num % 16
            if digit < 10:
                hex.append(str(digit))
            else:
                hex.append(chars[digit - 10])
            num = (num - digit) // 16
        
        return "".join(hex[::-1])

sol = Solution()
print(sol.toHex(26))
print(sol.toHex(-1))
print(sol.toHex(-2))
print(sol.toHex(0))