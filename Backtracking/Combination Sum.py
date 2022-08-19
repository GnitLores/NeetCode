from typing import List


class Solution:
    # Recursive depth first search solution.
    # Similar to solution for the Subsets problem, but here the same value may be included twice.
    # The tricky part is avoiding duplicate sets.
    # To avoid duplicates, we make the decision between including the current leftmost value
    # and not allowing the current leftmost value to be included.
    # O(n * 2^n) time.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        combination = []
        def findSum(i, total):
            # i: leftmost value that can be included
            # total: current sum
            if i >= len(candidates) or total > target:
                return
            if total == target:
                res.append(combination.copy())
                return
            
            combination.append(candidates[i])
            findSum(i, total + candidates[i])
            combination.pop()
            findSum(i+1, total)
            
        findSum(0, 0)
        return res

def testSolution(*args):
    sol = Solution()
    result = sol.combinationSum(*args)
    print(result)

testSolution([2,3,6,7], 7)