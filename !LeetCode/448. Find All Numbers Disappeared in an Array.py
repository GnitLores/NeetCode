from typing import List


class Solution:
    # Constant space solution from leetcode.
    # Since we know that there will be as many numbers as the greatest number,
    # we can use the numbers as indices and make those numbers negative.
    # This means that missing numbers will not be used and the corresponding
    # index positions will be positive.
    # O(n) time and O(1) space.
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])
        return [idx for idx, n in enumerate(nums, start=1) if n > 0] # Use 1 indexing to get correct numbers

    # Solution using set.
    # O(n) time but also O(n) space.
    def findDisappearedNumbersSet(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        res = []
        for i in range(1, n + 1):
            if i not in nums:
                res.append(i)
        return res

sol = Solution()
print(sol.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))
print(sol.findDisappearedNumbers([1,1]))
print(sol.findDisappearedNumbersSet(nums = [4,3,2,7,8,2,3,1]))
print(sol.findDisappearedNumbersSet([1,1]))