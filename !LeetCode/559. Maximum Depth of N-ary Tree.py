class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # Depth first search solution with post order traversal.
    # For each node, find the height of the subtree with that node as root
    # by adding one to the max height of the subtrees starting at each child node.
    def maxDepth(self, root: Node) -> int:
        if not root: return 0

        def dfs(root: Node):
            if not root.children: return 1

            maxSubTreeHeight = 0
            for node in root.children:
                maxSubTreeHeight = max(maxSubTreeHeight, dfs(node))
            return 1 + maxSubTreeHeight

        return dfs(root)

sol = Solution()
print(sol.maxDepth(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))