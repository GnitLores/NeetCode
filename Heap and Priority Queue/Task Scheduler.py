from typing import List
import heapq
import collections

class Solution:
    # Solution using heap and queue.
    # Start by counting the occurrences of each letter in O(n) time.
    # Then heapify the count (negative to make minheap maxheap).
    # We actually don't need to handle the letters again.
    # The important part is just the number of occurrences of distinct tasks.
    # We want to prioritize tasks with more occurrences while only making them
    # available when the cooldown on them is up.
    # (When tasks have equal prioriy, least recently issued tasks should go first,
    # but I think this happens automatically when pushing to the heap.)
    # Track time, pop highest priority task from heap, decrement the count,
    # calculate the time at which it will become available and add count and time to queue.
    # When queue task is available, push it back in the heap.
    # Pushing on heap is normall O(logn) but since we only have 26 letters, the worst case is
    # actually O(log26) = O(1).
    # The total complexity is then O(n * m) where m is the idle time. However, m is constrained so:
    # O(n) time.
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = dict()

        for t in tasks:
            counts[t] = counts.get(t, 0) + 1 # Count tasks
        heap = [-x for x in list(counts.values())] # Invert to make max heap
        heapq.heapify(heap)
        
        time = 0
        queue = collections.deque()
        
        while heap or queue:
            time += 1

            if heap:
                cnt = heapq.heappop(heap) + 1 # decrement count (plus because numbers are inverted)
                if cnt:
                    queue.append([cnt, time + n]) # push to queue with time it becomes available
            
            if queue and queue[0][1] == time: # If the next queue task is available
                heapq.heappush(heap, queue.popleft()[0]) # pop and push back on heap
        
        return time

sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2))