from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Preorder traversal evaluates the root first, then left subtree, and then the right subtree.
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []

        def preOrderDfs(root: TreeNode):
            res.append(root.val)
            if root.left:
                preOrderDfs(root.left)
            if root.right:
                preOrderDfs(root.right)

        preOrderDfs(root)
        return res


sol = Solution()
print(sol.preorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
print(sol.preorderTraversal(None))
print(sol.preorderTraversal(TreeNode(1)))
