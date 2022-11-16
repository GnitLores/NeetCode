import collections
from typing import List


class Solution:
    # If we count all the occurrences, the problem reduces to finding
    # the greatest common denominator of the group sizes.
    # For example, if we have the group sizes 4 and 6, we can divide them in groups of 2.
    # The gcd between two numbers a and b can be found by repeatedly setting a to b, and
    # setting b to a mod b.
    # When b reaches 0, a is the gcd.
    # We can then apply that for all the group sizes, finding the gcd for the current gcd
    # the next group size.
    # The problem requires the gcd to be greater than 1.
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd (a, b):
            if (b == 0):
                return a
            else:
                return gcd(b, a % b)

        counts = list(collections.Counter(deck).values())
        res = counts[0]
        for c in counts[1::]:
            res = gcd(res, c)
        return res > 1

sol = Solution()
print(sol.hasGroupsSizeX(deck = [1,2,3,4,4,3,2,1]))
print(sol.hasGroupsSizeX(deck = [1,1,1,2,2,2,3,3]))