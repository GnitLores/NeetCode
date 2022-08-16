from typing import List


class Solution:
    # Similar principle to Search Rotaed Sorted Array problem.
    # If midpoint is left of wrapping point, everything to the left is sorted - and conversely.
    # The minimum value is the first element after the wrapping point,
    # so keep looking for the wrapping point.
    # O(logn) time.
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if l == r:
                return nums[l]

            mid = (r + l) // 2 

            if nums[l] <= nums[mid] <= nums[r]: # No wrap
                return nums[l]
            
            if nums[l] <= nums[mid]: # Left sorted, wrap in right
                l += 1
            else: # Right sorted, wrap in left
                r -= 1

sol = Solution()
print(sol.findMin([0,1,2,4,5,6,7]))
print(sol.findMin([4,5,6,7,0,1,2]))
print(sol.findMin([3,4,5,1,2]))
print(sol.findMin([4,5,6,7,0,1,2]))
print(sol.findMin([11,13,15,17]))