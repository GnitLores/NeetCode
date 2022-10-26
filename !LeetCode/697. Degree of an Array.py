import collections
from typing import List


class Solution:
    # Solution using dictionaries.
    # For a subarray to have the same degree as the full array, the subarray must contain
    # all occurrences of the number with the greatest frequences.
    # The shortest subarray is the one that starts and ends with the first and last
    # occurrence of the highest frequency number.
    # The only complication is that multiple numbers with the same frequency may exist,
    # in which case we need to select the number where the first and last occurrences
    # are closest together for our subarray.
    #
    # Map each number to the count and the index of the first occurrence of that number.
    # Track the current degree, and the current shortest length subarray of that degree.
    # If the count equals the current degree, we have found a number with equal frequency
    # to the current greatest frequency (so far). In that case, check if the length of
    # the new subarray is shorter.
    # If the count is greater than the current degree, this is the new degree, and this
    # must be the new shortest subarray of that degree.
    # O(n) time.
    
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0
        minLen = len(nums)
        counts = collections.defaultdict(int)
        numFirst = collections.defaultdict(int)
        for i, n in enumerate(nums):
            counts[n] += 1
            if not n in numFirst:
                numFirst[n] = i
            count = counts[n]

            if count == degree:
                minLen = min(minLen, i - numFirst[n] + 1)
            if count > degree:
                degree = count
                minLen = i - numFirst[n] + 1
        return minLen

sol = Solution()
print(sol.findShortestSubArray(nums = [1,2,2,3,1]))
print(sol.findShortestSubArray(nums = [1,2,2,3,1,4,2]))
print(sol.findShortestSubArray(nums = [2]))