from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # Depth first search.
    # For each node, explore the subtrees first, and then append the
    # value of the node itself to the output.
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []
        def dfs(root: Node):
            if root.children:
                for node in root.children:
                    dfs(node)
            res.append(root.val)
            
        dfs(root)
        return res

sol = Solution()
print(sol.postorder(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))