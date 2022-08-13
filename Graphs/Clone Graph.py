
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Solution using rcursive depth first search and dictionary.
# Map old nodes to new nodes in the dictionary.
# If an old node has already been added to the dictionary,
# just return the new node from the dictionary instead of creating a new.
# This prevents looping indefinitely creating nodes.
# O(n) time where n is nodes + vertices.
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        oldToNew = dict()

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            newNode = Node(node.val)
            oldToNew[node] = newNode

            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))

            return newNode

        return dfs(node)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
sol = Solution()
res = sol.cloneGraph(node1)

res = sol.cloneGraph(Node(1))
res = sol.cloneGraph([])