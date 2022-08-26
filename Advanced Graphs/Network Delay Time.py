from typing import List
import collections
import heapq

class Solution:
    # Solution using Dijkstra's shortest bath algorithm.
    # BFS with min-heap.
    # From the starting node, add all adjacent nodes to a minheap ordered by the path length.
    # The pathlength to add is the path to the current node, plus the path to the added node.
    # Once a node is visited, pop from the heap until we find an unvisited node.
    # This way we only ever visit each node from the shortest path.
    # O((E+V) * log V^2) = O((E+V) * logV)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency = collections.defaultdict(set)
        for t in times:
            adjacency[t[0]].add((t[1], t[2]))

        heap = []
        visited = set()
        maxTime = 0
        node = k
        path = 0
        while len(visited) < n:
            while node in visited:
                if len(heap) == 0:
                    return -1
                path, node = heapq.heappop(heap)
            

            for a, t in adjacency[node]:
                if a not in visited:
                    newPath = path + t
                    heapq.heappush(heap, (newPath, a))

            maxTime = max(maxTime, path) # We only visit nodes from the shortest path to it, so the max of those is the total time.
            visited.add(node)
        return maxTime

sol = Solution()
print(sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
print(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
print(sol.networkDelayTime(times = [[1,2,1],[2,1,3]], n = 2, k = 2))