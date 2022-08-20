from typing import List
import collections

class Solution:
    # Topological sort.
    # Map courses to dependencies with a hashmap.
    # Do a DFS from each node, and when finding a bottom node (no dependencies),
    # add it to the output.
    # Remove the node as a dependency.
    # Record if a cycle is found and if so - return empty array.
    # O(n + v) time.
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses <= 1: return [0]
        hashmap = collections.defaultdict(set)
        for p in prerequisites:
            hashmap[p[0]].add(p[1])

        res = []
        visiting = set()
        completed = set()
        cycleFound = [False]
        def dfs(course):
            if course in completed or cycleFound[0] == True:
                return

            if course in visiting:
                cycleFound[0] = True
                return

            visiting.add(course)
            while hashmap[course]:
                dfs(hashmap[course].pop())
            visiting.remove(course)

            res.append(course)
            completed.add(course)
            return

        for i in range(numCourses):
            dfs(i)
        
        if cycleFound[0]:
            return []
        else:
            return res

sol = Solution()
print(sol.findOrder(2, [[1,0]]))
print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(sol.findOrder(1, []))