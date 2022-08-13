from typing import List

# Recursive depth first search through the decision tree.
# Keep the result set and the current subset as outer scope variables.
# For each element of the input, carry out both the decision to include and not include.
# Recursively carry out subsequent decisions.
# When reaching the bottom node of the decision tree, add the current subset to the result set.
# O(2^n * n) time, since there are two choices for each element.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        def findCombinations(i):
            if i >= len(nums):
                res.append(subset.copy()) # Need to copy as the subset will change after
                return
            
            # Decision to include element:
            subset.append(nums[i])
            findCombinations(i+1)

            # Decision not to include element:
            subset.pop()
            findCombinations(i+1)

        findCombinations(0)
        return res

def testSolution(*args):
    sol = Solution()
    result = sol.subsets(*args)
    print(result)

testSolution([1,2,3])