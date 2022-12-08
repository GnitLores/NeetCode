from typing import List


class Solution:
    # Iterate in steps of two and append generated array.
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            res += [nums[i + 1]] * nums[i]
        return res

sol = Solution()
print(sol.decompressRLElist(nums = [1,2,3,4]))
print(sol.decompressRLElist(nums = [1,1,2,3]))