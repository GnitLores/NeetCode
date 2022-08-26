import math

class Solution:
    # Solving this in python is tricky because arbitrary size integers are allowed,
    # which means that there is no overflow to detect, and because mod and integer division
    # with negative numbers do not work as in c/c++, so we have to do floating point and
    # cast to int. Python rounds toward -inf while c/c++ rounds towards zero.
    #
    # We can check for 32 bit overflow by checking if the intermediate result exceeds
    # the limits without the last digit, or if it is equal to it, if the digit to append
    # exceeds the last digit of the limit.
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10):
                return 0
            res = (res * 10) + digit

        return res

        

sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(120))