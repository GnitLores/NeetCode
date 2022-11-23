from typing import List


class Solution:
    # Convert to integer so we don't have to handle addition ourselves.
    # Sum powers to convert list to integer representation, add k to integer,
    # and then use modulo and integer division method to convert back into
    # list of numbers.
    # This is simple but unfortunately also slow and only barely passes leetcode.
    def addToArrayFormSimple(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        val = 0
        for i, n in enumerate(num):
            val += n * (10 ** i)
        val += k

        res = []
        while val > 0:
            digit = val % 10
            val //= 10
            res.append(digit)
        res.reverse()
        return res

sol = Solution()
print(sol.addToArrayFormSimple(num = [1,2,0,0], k = 34))
print(sol.addToArrayFormSimple(num = [2,7,4], k = 181))
print(sol.addToArrayFormSimple(num = [2,1,5], k = 806))