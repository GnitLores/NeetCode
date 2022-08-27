from typing import List


class Solution:
    # Observation: If we calculate a running maximum height from both left and right,
    # the minimum of those at any position is going to be the water level.
    # This means that we can simply subtract the height from the water level to get
    # the amount of water trapped at that point between higher points to the left and right.
    # O(n) time.
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0

        # Calculate running maximums
        maxFromLeft = [0] * len(height)
        maxLeft = 0
        maxFromRight = [0] * len(height)
        maxRight = 0
        for i in range(len(height)):
            maxLeft = max(height[i], maxLeft)
            maxFromLeft[i] = maxLeft
            maxRight = max(height[-1 - i], maxRight)
            maxFromRight[-1 - i] = maxRight

        trapped = 0
        for i in range(len(height)):
            waterLevel = min(maxFromLeft[i], maxFromRight[i])
            trapped += waterLevel - height[i]

        return trapped

    # Neetcode solution.
    # They had the exact same idea but implemented it as a two pointer solution.
    # We move the pointers based on the same principle as in the Container with Most Water problem.
    # If one position is higher than the other, we always move the lower height pointer.
    # If both are equal height, it doesn't matter which we move.
    # While moving the pointers towards the middle, we track the running left and right maximums.
    # This uses constant extra space, but it is not as efficient on leetcode.
    # O(n) time and O(1) space.
    def trapTwoPointer(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap([4,2,0,3,2,5]))
print(sol.trap([5,4,1,2]))
print(sol.trap([4,2,0,3,2,4,3,4]))
print("")
print(sol.trapTwoPointer([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trapTwoPointer([4,2,0,3,2,5]))
print(sol.trapTwoPointer([5,4,1,2]))
print(sol.trapTwoPointer([4,2,0,3,2,4,3,4]))