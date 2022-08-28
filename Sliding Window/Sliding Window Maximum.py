import collections
from typing import List


class Solution:
    # Sliding window solution using a queue.
    # This will be a monotonically decreasing queue - it can only contain non increaing values.
    # If we encounter a value lower than or equal to the current maximum, there is no issue.
    # If we encounter a greater value, that means that all smaller values currently existing in
    # the queue will no longer we possible maxima, and we can remove them.
    # This specific implementation stores indices in the queue and not the values themselves.
    # We have to do fewer operations this way.
    # The number pointed to by the leftmost index in the queue is the current maximum.
    # Since we remove indices pointing to smaller numbers than those added later, this will always be true.
    # O(n) time. If we had just found the max of the window it would have been O((n-w) * w).
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        queue = collections.deque() # queue of indices
        l = r = 0

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]: # If the new number is greater than the most recently added number
                queue.pop() # Pop from right until this is no longer the case as they will never be maxima
            queue.append(r) # Append index of new number

            if l > queue[0]: # If we are moving the left side of the window beyond the leftmost index in the queue, pop it
                queue.popleft()
            
            if (r + 1) >= k: # Initially we are just filling up our window, but once we have a full window:
                output.append(nums[queue[0]]) # Start adding the maximal value to the output.
                l += 1 # Only start sliding the window once it is fully formed.
            r += 1

        return output

sol = Solution()
print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(sol.maxSlidingWindow(nums = [1], k = 1))