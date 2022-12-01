from typing import List


class Solution:
    # Since there are only a limited number of possible heights, we can also solve this with
    # a counting sort, which is algorithmically superior to a comparison sort.
    # Count the number of occurrences of all hights from 1 to 100, and then iterate through them
    # an check how many times the order disagrees with the input heights.
    def heightCheckerCountingSort(self, heights: List[int]) -> int:
        count = [0] * 101
        for n in heights:
            count[n] += 1
        res = 0 # Number of disagreements
        i = 0 # Current index in heights
        for n, c in enumerate(count): # For count c of height n
            for _ in range(c): # Iterate in heights and check as many times as there were occurrences of n
                if n != heights[i]: res += 1
                i += 1
        return res

    # Intuitive solution using sorting.
    # Check each index against sorted array and sum number of differences.
    # Very simple and highly efficient on leetcode testcases, but not algorithmically optimal.
    # O(nlogn)
    def heightCheckerComparisonSort(self, heights: List[int]) -> int:
        return sum(x1 != x2 for x1, x2 in zip(heights, sorted(heights)))

sol = Solution()
print(sol.heightCheckerCountingSort(heights = [1,1,4,2,1,3]))
print(sol.heightCheckerCountingSort(heights = [5,1,2,3,4]))
print(sol.heightCheckerCountingSort(heights = [1,2,3,4,5]))
print("")
print(sol.heightCheckerComparisonSort(heights = [1,1,4,2,1,3]))
print(sol.heightCheckerComparisonSort(heights = [5,1,2,3,4]))
print(sol.heightCheckerComparisonSort(heights = [1,2,3,4,5]))