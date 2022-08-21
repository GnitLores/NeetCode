# Given n nodes labeled from 0 to n - 1 and a list of undirected edges
# (each edge is a pair of nodes), write a function to check whether these
# edges make up a valid tree.

from typing import List


class Solution:
    # Solution using Find-Union algorithm (see Redundant Connection problem).
    # For a tree to be valid, it must join in a set with a single unique parent and have no cycles.
    # Could also have been done with DFS in O(V + E time).
    # O(nlogn) time converging to O(n).
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            p = par[node]

            while p != par[p]:
                par[p] = par[par[p]]
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
        
        hasCycle = False
        for node1, node2 in edges:
            if not union(node1, node2):
                hasCycle = True

        uniqueParent = len(set(par)) == 1
        return uniqueParent and not hasCycle

sol = Solution()
print(sol.valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(sol.valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(sol.valid_tree(7, [[0, 1], [0, 2], [0, 3], [1, 4], [5, 6]]))