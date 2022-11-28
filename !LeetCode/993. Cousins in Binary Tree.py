from typing import Optional
from CreateBinaryTree import *

class Solution:
    # Depth first search.
    # Add tuple with information about matching nodes to list.
    # Break off search when two matches are found.
    # Check if parent are different and levels equal.
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        vals, n = (x, y), []
        def dfs(root: TreeNode, parent: TreeNode, level: int):
            if root.val in vals: n.append((parent, level))
            if len(n) == 2: return
            if root.left: dfs(root.left, root, level + 1)
            if root.right: dfs(root.right, root, level + 1)

        dfs(root, None, 0)
        return n[0][0] != n[1][0] and n[0][1] == n[1][1]

sol = Solution()
print(sol.isCousins(buildTree([1,2,3,4]), x = 4, y = 3))
print(sol.isCousins(buildTree([1,2,3,None,4,None,5]), x = 5, y = 4))
print(sol.isCousins(buildTree([1,2,3,None,4]), x = 2, y = 3))