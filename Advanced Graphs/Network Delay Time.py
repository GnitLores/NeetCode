from typing import List
import collections
import heapq

class Solution:
    # Solution using Dijkstra's shortest bath algorithm.
    # BFS with min-heap.
    # From the starting vertex, add all adjacent vertices to a minheap ordered by the path length.
    # The pathlength to add is the path to the current vertex, plus the path to the added vertex.
    # Once a vertex is visited, pop from the heap until we find an unvisited vertex.
    # This way we only ever visit each vertex from the shortest path.
    # O((E+V) * logV^2) = O((E+V) * logV)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency = collections.defaultdict(set)
        for t in times:
            adjacency[t[0]].add((t[1], t[2]))

        heap = []
        visited = set()
        maxTime = 0
        vertex = k
        path = 0
        while len(visited) < n:
            while vertex in visited:
                if len(heap) == 0:
                    return -1
                path, vertex = heapq.heappop(heap)
            

            for a, t in adjacency[vertex]:
                if a not in visited:
                    newPath = path + t
                    heapq.heappush(heap, (newPath, a))

            maxTime = max(maxTime, path) # We only visit vertices from the shortest path to each, so the max of those paths is the total time.
            visited.add(vertex)
        return maxTime

sol = Solution()
print(sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
print(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
print(sol.networkDelayTime(times = [[1,2,1],[2,1,3]], n = 2, k = 2))