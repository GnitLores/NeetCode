from typing import List
import math

class Solution:
    def jump(self, nums: List[int]) -> int:
        nums.reverse()
        jumpsNeeded = [0]*len(nums)
        for i in range(1, len(nums)):
            jumpLength = nums[i]
            if jumpLength == 0:
                jumpsNeeded[i] = math.inf
                continue
            maxLanding = max(i - jumpLength, 0)
            possibleJumps = jumpsNeeded[maxLanding:i]
            bestJump = min(possibleJumps)
            jumpsNeeded[i] = bestJump + 1
        return jumpsNeeded[-1]

sol = Solution()
# print(sol.jump([3,3,3,3,4]))
print(sol.jump([2,3,0,1,4]))
# print(sol.canJump([3,2,1,0,4]))