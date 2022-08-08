import heapq

# Solution using minimum heap.
# Building the heap is O(n) time.
# Adding elements is O(log n) time.
# Reading the kth largest element is O(1) time.
class KthLargest(object):
    def __init__(self, k, nums):
        self.k, self.minheap = k, nums
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val):
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]

def testSolution(k, nums, additional):
    obj = KthLargest(k, nums)
    for n in additional:
        print(str(n) + " added: " + str(obj.add(n)))

testSolution(3, [4, 5, 8, 2], [3, 5, 10, 9, 4])

