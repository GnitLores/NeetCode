from typing import List

# Iterate backwards through the array (exluding the goal).
# Increment the distance to the last element that could reach the goal.
# If the current jump length is greater than that distance, reset the distance.
# If the distance is 0 for the starting element, the goal is reachable.
# O(n) time.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()
        currentDistance = 0
        for n in nums[1:]:
            currentDistance += 1
            if n >= currentDistance:
                currentDistance = 0
        
        return currentDistance == 0

sol = Solution()
print(sol.canJump([2,3,1,1,4]))
print(sol.canJump([3,2,1,0,4]))
