from typing import List

# Recursive depth first search solution.
# Pass along the values possible to add, and call recursively with every value added.
# O(n!) time.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        def findPermutation(remaining):
            if len(remaining) == 0:
                res.append(subset.copy())
                return
            for i in range(len(remaining)):
                rem = remaining.copy()
                val = rem[i]
                rem.pop(i)
                subset.append(val)
                findPermutation(rem)
                subset.pop()

        findPermutation(nums)
        return res

def testSolution(*args):
    sol = Solution()
    result = sol.permute(*args)
    print(result)

testSolution([1,2,3])