from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Depth first search solution.
    # Pass along current value and when finding a leaf, add current value to output.
    # Since higher nodes are more significant, the deeper we go in the tree, the more significant
    # the higher nodes are.
    # Multiply the current value by 2 for every level we descend and add the next node.
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(root, cur):
            cur *= 2
            cur += root.val
            if not root.left and not root.right:
                res.append(cur)
                return
            if root.left: dfs(root.left, cur)
            if root.right: dfs(root.right, cur)
        dfs(root, 0)
        return sum(res)