import heapq
# Solution using heap priority queue.
# Pyhons heapq is implemented as a min heap, but we need max heap.
# Making all the weights negative effectively makes it a max heap.
# Building the heap is O(n) time.
# Pushing intermediate results is O(logn) time.
# accessing the heap is O(1) time.
class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [i*-1 for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 != stone2:
                res = abs(stone1 - stone2) * -1
                heapq.heappush(stones, res)
                
        if stones:
            return stones[0] * -1
        else:
            return 0

def testSolution(*args):
    obj = Solution()
    res = obj.lastStoneWeight(*args)
    print(str(res))

testSolution([2,7,4,1,8,1])
testSolution([1])