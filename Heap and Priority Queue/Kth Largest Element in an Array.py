from typing import List
import heapq

class Solution:
    # Solution using heap.
    # Invert values to make minheap work as maxheap.
    # O(n) to build heap, O(klogn) to get values.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)

        res = 0
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res

    # Quickselect solution.
    # Similar to quicksort but only works on one side of the pivot.
    # Select rightmost element as pivot and compare all other values.
    # If smaller or equal, swap with values in left side of array (at ptr).
    # If greater, leave in place.
    # Finally, swap pivot for value at ptr.
    # This results in all values <= pivot being to the left of the pivot,
    # and all values > than pivot being to the right.
    # Select side and repeat until the pivot value is placed at kth place from end.
    # This value is the kth greatest value.
    # O(n) time average for random values. O(n^2) worst case time.
    def findKthLargestQuickSelect(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[r]
            ptr = l
            for i in range(l, r):
                if nums[ptr] <= pivot:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[r], nums[ptr] = nums[ptr], nums[r]

            if ptr > k:   return quickSelect(l, ptr - 1)
            elif ptr < k: return quickSelect(ptr + 1, r)
            else:         return nums[ptr]

        return 0

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))