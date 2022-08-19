from typing import List


class Solution:
    # Combination of solutions to Subsets II and Combination Sum problems.
    # From subsets II:
    # If there are duplicates, then if a number has been included, the subtree for that decision
    # includes all combinations in the subtree without the inclusion where the other occurrences are included.
    # As in Combination Sum, we pass along a total and check for the target.
    # O(n * 2^n) time.
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res =  []
        subset = []
        def findCombinations(i, total):
            if total == target:
                res.append(subset.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            subset.append(candidates[i])
            findCombinations(i + 1, total + candidates[i])
            subset.pop()

            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            findCombinations(i + 1, total)

        findCombinations(0, 0)
        return res

sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
print(sol.combinationSum2([2,5,2,1,2], 5))
print(sol.combinationSum2([5], 5))
print("")