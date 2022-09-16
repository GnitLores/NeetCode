from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Inorder traversal evaluates the left subtree first, then the root, then the right subtree.
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        def inOrderDfs(root: TreeNode):
            if root.left: inOrderDfs(root.left)
            res.append(root.val)
            if root.right: inOrderDfs(root.right)
        inOrderDfs(root)
        return res

sol = Solution()
print(sol.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
print(sol.inorderTraversal(None))
print(sol.inorderTraversal(TreeNode(1)))