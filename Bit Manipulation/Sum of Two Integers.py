class Solution(object):
    # Adding two numbers is equivalent XORing them and then adding the carries.
    # Carries can be found by ANDing the numbers together.
    # To move the carries to the bit they carry to, bitshift left by 1.
    # Adding the carries is also itself an addition.
    # So this is an iterative process that continues until nothing carries.
    #
    # 2 + 3 = 5:
    # 0 0 1 0  
    # 0 0 1 1
    #
    # 0 0 0 1 XOR
    # 0 1 0 0 AND << 1
    # XORing these gives
    # 0 1 0 1 = 5
    # And there is no carry
    #
    # Additionally, python does not handle integers like many other languages.
    # Python integers are arbitrarily large, not 32 bit. Negative values have leading ones.
    # We can use a mask 0xffffffff = 32 ones to force the numbers to 32 bit by ANDing.
    # We then also have to handle negative results, which are represented differently in python.
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while b != 0: # On iterations other than the first, check if there is carry:
            tmp = (a & b) << 1 # Find carrying bits and shift
            a = (a ^ b) & mask # XOR
            b = tmp & mask

        if a > mask // 2: # If the answer is negative integer (mask // 2 is greatest number before leftmost bit becomes 1 which means it is negative)
            return ~(a ^ mask) # XORing with 1 flips a bit, so XORing with the mask flips the 32 rightmost bits. NOT then flips them back along with all the making the leading 0s into leading 1s.
        else:
            return a

sol = Solution()
print(sol.getSum(1, 2))
print(sol.getSum(2, 3))
print(sol.getSum(6, 3))
