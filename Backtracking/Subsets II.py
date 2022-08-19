from typing import List


class Solution:
    # Observation: if input elements are ordered, then in combinations that have the same elements,
    # the elements will be in the same order.
    # This means that we can add them to a set to get unique combinations.
    # This does not work with unordered input because identical combinations with different order hash differently.
    # Sorting is O(n) which is faster than the overall complexity.
    # O(2^n * n) time, since there are two choices for each element.
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()
        subset = []
        def findcombinations(i):
            if i >= len(nums):
                res.add(tuple(subset.copy())) # Must be tuple to hash
                return

            subset.append(nums[i])
            findcombinations(i + 1)

            subset.pop()
            findcombinations(i + 1)

        findcombinations(0)

        res = [list(x) for x in list(res)] # Convert back to lists
        return res

    # Observation:
    # If there are duplicates, then if a number has been included, the subtree for that decision
    # includes all combinations in the subtree without the inclusion where the other occurrences are included.
    # Ex: if 2 is included, then the "yes" subtree includes all combinations with both one and more 2s.
    # Thus we can exclude all other 2s from the "no" subtree.
    # Also relies on sort and has similar complexity but omits some computations.
    def subsetsWithDupRejectDuplicates(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        subset = []
        def findcombinations(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            findcombinations(i + 1)
            subset.pop()

            # For the "no" decision: iterate i to exclude duplicates. Works because input is sorted.
            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            findcombinations(i + 1)

        findcombinations(0)

        return res

sol = Solution()
print(sol.subsetsWithDup([1,2,2]))
print(sol.subsetsWithDup([0]))
print("")
print(sol.subsetsWithDupRejectDuplicates([1,2,2]))
print(sol.subsetsWithDupRejectDuplicates([0]))