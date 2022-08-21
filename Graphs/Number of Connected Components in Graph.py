# Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
# (each edge is a pair of nodes), write a function to find 
# the number of connected components in an undirected graph.
# Example 1:
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#      0          3
#      |          |
#      1 --- 2    4 
# Output: 2
# Example 2:
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#      0           4
#      |           |
#      1 --- 2 --- 3
# Output:  1
# Note:
# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] and 
# thus will not appear together in edges.

from typing import List


class Solution:
    # Solution using Union-Find algorithm with path compression and union by rank
    # (see Redundant Connection problem).
    # Each remaining set has its own top parent,
    # so the number of parents is the number of disjoint graphs.
    # Path compression makes the find operation O(logn) converging
    # to O(1) with repeated callse instead of O(n).
    # Union by rank is O(1).
    # This makes the total complexity O(nlogn) converging to O(n) instead of O(n^2).
    # Doing Union-Find by rank with path compression Could also have been done with DFS in O(e + v) time.
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            p = par[node]

            while p != par[p]:
                par[p] = par[par[p]] # path compression
                p = par[p]
            return p

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for node1, node2 in edges:
            union(node1, node2)
        
        nrOfParents = len(set(par))
        return nrOfParents

sol = Solution()
print(sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
print(sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))