from typing import List


class Solution:
    # Create ranks.
    # Create indices of scores and sort them by score in descending order.
    # Assign each rank to the appropriate index.
    # O(nlogn).
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(score) + 1)))

        idxByScore = [i for _, i in sorted(zip(score, range(len(score))), reverse = True)]
        res = [None] * len(score)
        for i in range(len(score)):
            res[idxByScore[i]] = ranks[i]
        return res

sol = Solution()
print(sol.findRelativeRanks(score = [1]))
print(sol.findRelativeRanks(score = [5,4,3,2,1]))
print(sol.findRelativeRanks(score = [10,3,8,9,4]))