class Solution(object):
    # Iterate through and for each position:
    # Find the jump that enables the greatest distance on the subsequent jump.
    def jump(self, nums):
        if len(nums) == 1:
            return 0

        end = len(nums) - 1
        jumps = 0
        ptr = 0
        while ptr < end:
            jumps += 1

            bestJump = ptr
            jumpPtr = ptr
            while jumpPtr < min(ptr + nums[ptr], end): # Search all possible jumps from this position or to end of array if closer
                jumpPtr += 1

                if jumpPtr == end: # If end is reachable from this position
                    return jumps

                if jumpPtr + nums[jumpPtr] > bestJump + nums[bestJump]: # If this gives the best subsequent jump so far
                    bestJump = jumpPtr
            ptr = bestJump

sol = Solution()
print(sol.jump([3,3,3,3,4]))
print(sol.jump([2,3,0,1,4]))
print(sol.jump([2,3,2,0,1,1,1,1,4]))