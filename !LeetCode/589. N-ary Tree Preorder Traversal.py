from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # Depth first search.
    # For each node, add the node value to the output first, and then continue.
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []
        def dfs(root: Node):
            res.append(root.val)
            if not root.children: return
            for node in root.children:
                dfs(node)
            
        dfs(root)
        return res

sol = Solution()
print(sol.preorder(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))