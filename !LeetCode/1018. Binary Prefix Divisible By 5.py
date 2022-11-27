from typing import List


class Solution:
    # In each iteration, each bit shifts one space to the left becoming
    # more significant by a factor of 2.
    # Multiply the current number by 2 and add the new bit, and then check
    # if the new number is divisible by 5.
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        cur = 0
        for n in nums:
            cur *= 2
            cur += n
            res.append(cur % 5 == 0)
        return res

sol = Solution()
print(sol.prefixesDivBy5(nums = [0,1,1]))
print(sol.prefixesDivBy5(nums = [1,1,1]))