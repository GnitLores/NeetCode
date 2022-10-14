from typing import List


class Solution:
    # In order to maximize the sum of pair minima, we want to
    # pair small values together. If we pair a small value with a
    # larger value, the larger value is lost.
    # In effect, this means that we just want to sort the list in
    # ascending order and create pairs.
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(map(min, zip(nums[0::2], nums[1::2])))

sol = Solution()
print(sol.arrayPairSum(nums = [1,4,3,2]))
print(sol.arrayPairSum(nums = [6,2,6,5,1,2]))