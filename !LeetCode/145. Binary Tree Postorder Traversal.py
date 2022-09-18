from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Postorder traversal evaluates the left subtree first, then the right subtree, and then the root.
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        def postOrderDfs(root: TreeNode):
            if root.left: postOrderDfs(root.left)
            if root.right: postOrderDfs(root.right)
            res.append(root.val)
        postOrderDfs(root)
        return res

sol = Solution()
print(sol.postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
print(sol.postorderTraversal(None))
print(sol.postorderTraversal(TreeNode(1)))