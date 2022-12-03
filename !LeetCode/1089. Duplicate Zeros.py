from typing import List
from collections import deque

class Solution:
    # Can be solved with a queue.
    # For every element in the array, add it to the back of a queue,
    # and if it is a zero, add another zero.
    # Insert elements in the array from the front of the queue.
    # The queue grows by one element for every zero.
    def duplicateZeros(self, arr: List[int]) -> None:
        q = deque()
        i = 0
        while i < len(arr):
            val = arr[i]
            q.append(val)
            if val == 0: q.append(val)
            arr[i] = q.popleft()
            i += 1
        return arr

sol = Solution()
print(sol.duplicateZeros(arr = [1,0,2,3,0,4,5,0]))
print(sol.duplicateZeros(arr = [1,2,3]))