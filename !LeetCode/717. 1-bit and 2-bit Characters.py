from typing import List


class Solution:
    # The output is false in two cases:
    # IF the rightmost bit is 1.
    # IF the rightmost bit is 0 and this is followed by
    # an odd number of 1s.
    # This is because for the last two bits to be a two bit char,
    # it must be 10, and the next sequence of 1s must be all 11 chars.
    # There is no 01 or 1 chars, so the last 1 in the squence (tracking backwards)
    # cannot be anything other than a 11 char.
    # ...011110 = True (...0 11 11 0) is necessary, (...01 11 10) and ()...0 1 11 10) are not possible.
    # ...0111110 = False (...0 11 11 10) is possible.
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1: return True
        if bits[-1] == 1: return False
        if bits[-2] == 0: return True
        
        # Last two bits are [1, 0] - check of odd or even number of ones
        i = len(bits) - 2
        evenOnes = True
        while i >= 0 and bits[i] == 1:
            evenOnes = not evenOnes
            i -= 1

        return evenOnes

sol = Solution()
print(sol.isOneBitCharacter(bits = [1,0,0]))
print(sol.isOneBitCharacter(bits = [1,1,1,0]))