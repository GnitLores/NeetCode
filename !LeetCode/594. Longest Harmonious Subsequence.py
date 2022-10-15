import collections
from typing import List


class Solution:
    # The subsequence must consist of exactly two distinct values
    # that are different by 1.
    # Since any element can be deleted and the seuqence does not need to be
    # contiguous, all valid elements will be included in the subsequence.
    # We can count all values with a dictionary and for each unique value
    # check if that value +/- 1 was also counted.
    # If so the sum of counts for those two values is the length of a valid subsequence.
    # We then just need to find the longest valid subsequences.
    # O(n) time.
    def findLHS(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
        
        mxl = 0
        vals = set(count.keys())
        for n in vals:
            c = count[n]
            if n - 1 in vals: mxl = max(mxl, c + count[n - 1])
            if n + 1 in vals: mxl = max(mxl, c + count[n + 1])
        return mxl

sol = Solution()
print(sol.findLHS(nums = [1,3,2,2,5,2,3,7]))
print(sol.findLHS(nums = [1,2,3,4]))
print(sol.findLHS(nums = [1,1,1,1]))