from typing import List
import heapq

class Solution:
    # Solution using heap and sorting.
    # If we sort both the intervals by starting and the queries in ascending order, 
    # we can evaluate queries sequentially.
    # For each query, push every interval eith an earlier start time into a min heap
    # ordered by the interval length.
    # The current minimal interval could be an earlier interval which doesn't include the
    # current query, so pop from the heap until the first element does.
    # Peak at this value without popping it and add it to the output.
    # This works because the queries and intervalse are sorted.
    # If an interval ends before the current query, it will not include a later interval,
    # so it is safe to pop it from the heap.
    # 
    # A further complication is that the output must be return in the original query order.
    # Here I turn the queries into and index list of tuples, sort by the query, and then
    # in the end I sort the output by the original indices.
    # Alternatively, the indices could have been mapped with a dictionary.
    #
    # O(nlogn + qlogq) because we are sorting and pushing/popping from a heap.

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(x, i) for i, x in enumerate(queries)]

        intervals.sort()
        queries.sort()
        heap = []
        res = []
        
        i = 0
        for query in queries:
            while i < len(intervals) and query[0] >= intervals[i][0]:
                dur = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, [dur, intervals[i]])
                i += 1
            
            while heap and (query[0] < heap[0][1][0] or query[0] > heap[0][1][1]):
                heapq.heappop(heap)

            if heap:
                res.append((query[1], heap[0][0]))
            else:
                res.append((query[1], -1))

        res.sort()
        res = [x[1] for x in res]
        return res

sol = Solution()
print(sol.minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]))
print(sol.minInterval(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]))