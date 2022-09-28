# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int, pick: int) -> int:
        def guess(g):
            if g == pick: return 0
            if g < pick: return 1
            return -1
        
        l, r = 1, n
        while l <= r:
            m = l + (r - l) // 2
            res = guess(m)
            match res:
                case 1:
                    l = m + 1
                case -1:
                    r = m - 1
                case 0:
                    return m

sol = Solution()
print(sol.guessNumber(n = 10, pick = 6))
print(sol.guessNumber(n = 1, pick = 1))
print(sol.guessNumber(n = 2, pick = 1))