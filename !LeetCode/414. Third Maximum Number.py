import heapq
from typing import List


class Solution:
    # Solution using heap.
    # Make list unique by converting to set and back to list.
    # Negate all values and convert to minheap.
    # Since list is unique, the third element popped from the heap
    # will always be the third maximum.
    # If there are not three elements, pop and return the first maximum.
    # Heapifying is O(n), and while popping from the heap is O(logn), we
    # only do it a max of three times, so total O(n) time.
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums = [-x for x in nums]
        heapq.heapify(nums)
        
        if len(nums) >= 3:
            heapq.heappop(nums)
            heapq.heappop(nums)
            return -heapq.heappop(nums)
        else:
            return -heapq.heappop(nums)

sol = Solution()
print(sol.thirdMax(nums = [3,2,1]))
print(sol.thirdMax(nums = [1,2]))
print(sol.thirdMax(nums = [2,2,3,1]))