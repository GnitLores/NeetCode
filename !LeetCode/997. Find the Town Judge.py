from typing import List
from collections import Counter

class Solution:
    # Since we know that all the pairs are unique, we know that the judge
    # must be the person trusting 0 times and the person trusted n - 1 times.
    # Trusting is indicated in the left column and being trusted is indicated
    # in the right column.
    # Get the columns by unpacking and zipping, and the use counters
    # to check if any person fulfills the criteria.
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0: return 1 if n == 1 else -1
        trusts, trusted = list(zip(*trust))
        trusts, trusted = Counter(trusts), Counter(trusted)
        for i in range(1, n + 1):
            if trusts[i] == 0 and trusted[i] == n - 1:
                return i
        return -1

sol = Solution()
print(sol.findJudge(n = 2, trust = [[1,2]]))
print(sol.findJudge(n = 3, trust = [[1,3],[2,3]]))
print(sol.findJudge(n = 3, trust = [[1,3],[2,3],[3,1]]))