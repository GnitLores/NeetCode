from typing import List
import collections

class Solution:
    # Observation: the rendundant edge leads to a cycle. We know there is exactly one cycle.
    # Use DFS to detect edges that are in a cycle,
    # and remove the last input edge that was in a cycle.
    # All nodes are connected, so we only need to run DFS once and from any node.
    # O(n + e) time.
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        hashmap = collections.defaultdict(set)
        for e in edges: # Map connected nodes in both directions.
            hashmap[e[0]].add(e[1])
            hashmap[e[1]].add(e[0])

        cycle = set()
        visiting = set()
        def dfs(node):
            if node in visiting: # If this is the start of a cycle
                return True, node

            if not hashmap[node]: # If no edges to explore
                return False, None

            visiting.add(node)
            while hashmap[node]: # While there are unexplored edges:
                # Choose an edge and remove it from the map -
                # both for this node and the connected node.
                con = hashmap[node].pop()
                hashmap[con].remove(node)

                wasCycle, cycleStart = dfs(con) # Explore edge
                
                if wasCycle:
                    if node < con: # Edges are sorted
                        cycle.add((node, con))
                    else:
                        cycle.add((con, node))

                    visiting.remove(node)

                    # If we have returned to the cycle start, stop adding to the cycle and return.
                    if cycleStart == node: 
                        return False, None
                    else:
                        return True, cycleStart

            visiting.remove(node)
            return False, None
        
        # We only need to run DFS once
        dfs(edges[0][0])

        # Return the last edge in the input that was in a cycle:
        edges.reverse()
        for e in edges:
            if tuple(e) in cycle:
                return e

    # Could also have been solved using the Union-Find algorithm.
    # Union-Find can be used to detect cycle in an undirected graph.
    # Union-Find:
    # All nodes have a parent and rank.
    # The parent is the top node in the subset. The rank is the size of the subset.
    # At first, all nodes are their own parent and all ranks are 1.
    # For each edge:
    # Add the smaller subset to the larger subset.
    # This makes the nodes have the same parent and creates a new subset with greater rank.
    # If we try to add an edge but the two nodes already have the same parent,
    # this is a redundant connection. It is creating a cycle.
    # We also use path compression to compress the chain of parents.
    # Path compression makes the find operation O(logn) instead of O(n).
    # This makes the total complexity O(nlogn) instead of O(n^2).
    def findRedundantConnectionUnionFind(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)] # all nodes are their own parent
        rank = [1] * (len(edges) + 1) # All subsets have rank 1
        
        # Find the parent (top node) of a node:
        def find(n):
            p = par[n]

            while p != par[n]:
                # Path compression.
                # Compresses the chain of parents so that it is faster to traverse next time.
                par[p] = par[par[p]] 
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2) 

            if p1 == p2: # If they have the same parent, this is a cycle.
                return False
            
            # Join the smaller subset to the larger
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        # Try to join nodes from all edges:
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]




sol = Solution()
print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))
print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
print("")
print(sol.findRedundantConnectionUnionFind([[1,2],[1,3],[2,3]]))
print(sol.findRedundantConnectionUnionFind([[1,2],[2,3],[3,4],[1,4],[1,5]]))