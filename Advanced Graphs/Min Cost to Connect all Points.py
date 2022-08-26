from typing import List
import heapq

class Solution:
    # Solution using  Prim's algorithm for finding min spanning tree.
    # We have a set of node already visited and a minheap of nodes
    # that could be visited ordered by the cost of adding them.
    # We pop the least costly node, and if it has not been visited it,
    # we visit it and add all nodes that have not been visited to frontier.
    # This means that multiple connections to the same node can exist in the heap because
    # it may be adjacent to muplitple nodes we visit before it.
    # We find the cheapest one and dicard the others.
    # This results in the min spanning tree.
    # The implementation here is a bit simpler than usual because all nodes can connect.
    # Otherwise we would need a list of adjacent nodes for each node.
    # O(n^2 * logn) time and very efficient on leetcode.
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set() # set of pointNr already visited
        frontier = [] # minheap [cost, pointNr]
        cost = 0 # Total cost

        p = 0 # Start with point 0
        c = 0 # There is zero cost to adding point 0
        
        while len(visited) < len(points):
            while p in visited:
                c, p = heapq.heappop(frontier)
            visited.add(p)
            cost += c
            for i in range(len(points)):
                if i not in visited:
                    dist = abs(points[i][0] - points[p][0]) + abs(points[i][1] - points[p][1])
                    heapq.heappush(frontier, [dist, i])
        return cost

sol = Solution()
print(sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(sol.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))