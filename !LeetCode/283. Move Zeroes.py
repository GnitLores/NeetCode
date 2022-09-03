from typing import List


class Solution:
    # Solution using two pointer.
    # Iterate over the array while keeping a pointer to the leftmost zero.
    # Swap non zero elements to the right of the zero pointer with the zero pointer element.
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1: return
        zeroPtr = 0
        for i in range(len(nums)):
            while zeroPtr < len(nums) and nums[zeroPtr] != 0: # Search for first zero
                zeroPtr += 1
            if nums[i] != 0 and i > zeroPtr:
                nums[i], nums[zeroPtr] = nums[zeroPtr], nums[i] # Swap with leftmost zero
        return


sol = Solution()
sol.moveZeroes([0,1,0,3,12])
sol.moveZeroes([0])