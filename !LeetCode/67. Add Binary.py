from tkinter import Y


class Solution:
    # Solution making use of python's conversion functions.
    # int(x, 2) converts binary string to int, and
    # bin(x) can convert an int to binary representation.
    # We need to strip the two characters long prefix of the output string (0b101 -> 101).
    def addBinaryConversion(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    # Solution using output list.
    # Make list long enough to handle carry.
    # Go through bits from least significant to most.
    # For each bit in each number check if bit is 1.
    # If there is a 1, either add it to the output if output is zero, or
    # make input zero and add the carry to the next bit of the output.
    def addBinary(self, a: str, b: str) -> str:
        res = ["0" for _ in range(max(len(a), len(b)) + 1)]

        def addBit(i):
            if res[i] == "1":
                res[i] = "0"
                res[i + 1] = "1"
            else:
                res[i] = "1"

        for i in range(max(len(a), len(b))):
            if i < len(a) and a[-1 - i] == "1":
                addBit(i)
            if i < len(b) and b[-1 - i] == "1":
                addBit(i)

        if res[-1] == "0":
            res.pop()  # Remove most significant digit if there was no carry to it.
        return "".join(res)[::-1]


sol = Solution()
print(sol.addBinaryConversion(a="11", b="1"))
print(sol.addBinaryConversion(a="1010", b="1011"))
print("")
print(sol.addBinary(a="11", b="1"))
print(sol.addBinary(a="1010", b="1011"))
