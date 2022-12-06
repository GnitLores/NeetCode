import collections
import math
from typing import List


class Solution:
    # Turn dominoes into tuples and make each domino turn in the same direction.
    # This way they can be hashed and we can count the number of equivalent dominoes with
    # a counter.
    # Then we go through each unique domino and use the formula for combinations of size k in
    # n elements (k = 2 and n = number of dominoes) to find the number of combinations for each.
    def numEquivDominoPairsCombinationCount(self, dominoes: List[List[int]]) -> int:
        dominoes = [(d[0], d[1]) if d[0] <= d[1] else (d[1], d[0]) for d in dominoes]
        count = collections.Counter(dominoes)
        res = 0
        for d in count.keys():
            c = count[d]
            if c == 2:
                res += 1
            elif c > 2:
                factC = math.factorial(c)
                denom = math.factorial(2) * math.factorial(c - 2)
                res += factC // denom
        return res

sol = Solution()
print(sol.numEquivDominoPairsCombinationCount(dominoes = [[1,2],[2,1],[3,4],[5,6]]))
print(sol.numEquivDominoPairsCombinationCount(dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]))