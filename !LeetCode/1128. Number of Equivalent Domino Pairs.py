import collections
import math
from typing import List


class Solution:
    # Similar to the other solution, turn into sorted tuples and count.
    # This time we count as we go, so we use a dictionary instead of a counter.
    # For each domino, the number of combinations added by including the new domino
    # is equal to the number of dominoes of that type already included.
    # E.g if we already found 2 dominoes of a type there is already 1 combination possible,
    # and adding a third adds 2 new combinations for a total of 3.
    # This is faster and simpler than the other solution.
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = collections.defaultdict(int)
        res = 0
        for d in dominoes:
            d = (d[0], d[1]) if d[0] <= d[1] else (d[1], d[0])
            res += count[d]
            count[d] += 1
        return res

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
print(sol.numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[5,6]]))
print(sol.numEquivDominoPairs(dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]))
print("")
print(sol.numEquivDominoPairsCombinationCount(dominoes = [[1,2],[2,1],[3,4],[5,6]]))
print(sol.numEquivDominoPairsCombinationCount(dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]))