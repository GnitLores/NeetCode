# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Depth first search.
    # Pass along path string (immutable so no need to remove nodes again).
    # Add string to result at leaf nodes.
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root:
            return res

        def dfs(root, path):
            if not root:
                return
            path = str(root.val) if len(path) == 0 else "->".join([path, str(root.val)])
            if not root.left and not root.right:
                res.append(path)
            dfs(root.left, path)
            dfs(root.right, path)

        dfs(root, "")
        return res


sol = Solution()
print(sol.binaryTreePaths(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))))
print(sol.binaryTreePaths(TreeNode(1)))
print(sol.binaryTreePaths(None))
