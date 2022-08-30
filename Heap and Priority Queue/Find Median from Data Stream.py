import heapq

# Solution using two heaps.
# We know that if we partition the ordered array, the median is either
# the greatest value of the left partition or the smallest value of the
# right partition in the case of an odd number of values,
# or the average of those in the case of an even number of values.
# We use a maxheap for the left partition and a minheap for the right partition
# to always track these values.
# If one heap grows more than one value larger than the other, pop an element and
# push it on the other heap.
# We have to negate whenever interacting with the maxheap, as it
# is really a minheap working on negative values.
# Addnum is O(logn) and findMedian is O(1).
class MedianFinder:

    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []
        self.isOdd = False

    def addNum(self, num: int) -> None:
        if not self.leftHeap:
            heapq.heappush(self.leftHeap, -num)
        elif num > (-self.leftHeap[0]):
            heapq.heappush(self.rightHeap, num)
        else:
            heapq.heappush(self.leftHeap, -num)

        if len(self.leftHeap) > (len(self.rightHeap) + 1):
            heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))

        if len(self.rightHeap) > (len(self.leftHeap) + 1):
            heapq.heappush(self.leftHeap, -heapq.heappop(self.rightHeap))

        self.isOdd = not self.isOdd

    def findMedian(self) -> float:
        if self.isOdd:
            if len(self.leftHeap) > len(self.rightHeap):
                return -self.leftHeap[0]
            else:
                return self.rightHeap[0]
        else:
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

medianFinder = MedianFinder()
medianFinder.addNum(1)           # arr = [1]
medianFinder.addNum(2)           # arr = [1, 2]
print(medianFinder.findMedian()) # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)           # arr[1, 2, 3]
print(medianFinder.findMedian()) # return 2.0
medianFinder.addNum(5)
medianFinder.addNum(5)
medianFinder.addNum(8)
medianFinder.addNum(1)
print(medianFinder.findMedian()) 