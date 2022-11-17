from typing import List


class Solution:
    # Create empty output list and track the next indices for even and odd values.
    # Insert eeach value at next index depending on parity.
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        evenIdx, oddIdx = 0, 1
        for n in nums:
            if n % 2 == 0:
                res[evenIdx] = n
                evenIdx += 2
            else:
                res[oddIdx] = n
                oddIdx += 2
        return res

sol = Solution()
print(sol.sortArrayByParityII(nums = [4,2,5,7]))
print(sol.sortArrayByParityII(nums = [2,3]))