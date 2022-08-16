class Solution(object):
    # Linear time double pointer solution.
    # The key thing to realizes is that if one line is taller than the other, then there is no point in moving it.
    # Moving it closer can only make the area smaller.
    # So taking advantage of that fact, we can always move the shorter line closer looking for a greater area.
    # Both lines being equally tall is a special case.
    # There could still be a more optimal solution with the lines closer, and it doesn't matter which we move first.
    # O(n) time.
    def maxArea(self, height):
        
        def calcWater(l, r):
            return min(height[l], height[r]) * (r - l)

        l = 0
        r = len(height) - 1

        res = calcWater(l, r)
        while l < r:

            if height[l] <= height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            else:
                break

            res = max(res, calcWater(l, r))

        return res

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([2,3,10,5,7,8,9]))
print(sol.maxArea([2,3,4,5,18,17,6]))
