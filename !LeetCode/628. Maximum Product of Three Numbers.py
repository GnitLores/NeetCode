from typing import List
import heapq

class Solution:
    # Solution using heaps.
    # The only situation in which we would want to include minimum values
    # is if we have two negative minimum values that mulitply to a greater number
    # than two of the three max values.
    # In any case we will always include at most two min values,
    # and we will always include the max value.
    # In other words, it is a choice between including the two min values and
    # the second and third max value.
    # Make a min heap and a max heap.
    # Pop the max value.
    # Multiply that value by the next two values popped from either heap and
    # check what gives the greater result.
    # O(n) time because heapify is a O(n) operation and we only pop 5 times.
    def maximumProduct(self, nums: List[int]) -> int:
        minHeap = nums
        heapq.heapify(minHeap)
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)

        maxVal = -heapq.heappop(maxHeap)
        maxMax = -heapq.heappop(maxHeap) * -heapq.heappop(maxHeap) * maxVal
        minMax = heapq.heappop(minHeap) * heapq.heappop(minHeap) * maxVal
        res = max(maxMax, minMax)

        return res

sol = Solution()
print(sol.maximumProduct(nums = [1,2,3]))
print(sol.maximumProduct(nums = [1,2,3,4]))
print(sol.maximumProduct(nums = [-1,-2,-3]))
print(sol.maximumProduct(nums = [-1,-2,-3,-4]))