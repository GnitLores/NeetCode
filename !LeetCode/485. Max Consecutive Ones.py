from typing import List


class Solution:
    # I think the simplest way is just to record the max length.
    # You can do clever tricks with comprehensions, but they don't seem superior.
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        c = 0
        for n in nums:
            if n == 1:
                c += 1
                res = max(res, c)
            else:
                c = 0
        return res

sol = Solution()
print(sol.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
print(sol.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))