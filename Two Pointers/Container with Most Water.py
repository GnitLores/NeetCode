class Solution(object):
    def maxArea(self, height):
        
        def calcWater(l, r):
            return min(height[l], height[r]) * (r - l)

        l = 0
        r = len(height) - 1

        # if len(height) == 2:
        #     return(calcWater(l, r))

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
