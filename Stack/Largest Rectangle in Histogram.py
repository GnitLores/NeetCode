from typing import List


class Solution:
    # Solution using a stack.
    # Observations:
    # - When we encounter a bar taller than the last, this adds a new possible rectangle with greater height.
    # - When we encounter a bar with sam height as the last, this does not add a new possible rectangle.
    # - When we encounter a bar with shorter height than previous bars, taller rectangles before this
    # cannot continue beyond this point. However, rectangles with the same length but limited in height
    # by the new bar could.
    # Thus, when we get to a shorter height, we need to evaluate previous taller rectangles and readd new
    # height limited rectangles.
    # A stack is a suitable data structure for this.
    # We use a stack with each element [h, i] indicating the start of a rectangle with height h starting at index i.
    # When we encounter a shorter height, for each taller rectangle, pop it, calculate the area,
    # and record the max area. Then push it back unto stack but with the new lower height.
    # However, there is no point in having two rectangles of the same height but starting at
    # different times, so only add the earliest index for each unique rectangle.
    # Finally, when we have added all bars, calculate the area of all remaining rectangles.
    # Neetcode came to an identical solution and claims that it is O(n) time.
    # However, it seems to me that if all the bars are in decreasing order the worst case complexity might be O(n^2)
    # as each previous rectangle will change with every future bar.
    # At any rate, this runs very efficiently on leetcode.
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =  []
        
        maxRectangle = 0
        for i, h in enumerate(heights):
            h = heights[i]
            
            # Pop all previous rectangles taller than the current bar and calculate the the area.
            # Add a rectangle limited to the height of the current bar back on the stack.
            while stack and h < stack[-1][0]:
                hp, ip = stack.pop()
                size = hp * (i - ip)
                maxRectangle = max(maxRectangle, size)
                if not stack or h > stack[-1][0]: # Don't add multiple rectangles with same height.
                    stack.append([h, ip])

            # Add new rectangle with greater height than previous.
            if not stack or h > stack[-1][0]:
                stack.append([h, i])
        
        # Calculate all remaining rectangles
        for _ in range(len(stack)):
            hp, ip = stack.pop()
            size = hp * (len(heights) - ip)
            maxRectangle = max(maxRectangle, size)
                    
        return maxRectangle

sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))
print(sol.largestRectangleArea([2,4]))