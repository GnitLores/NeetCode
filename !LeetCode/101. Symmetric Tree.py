# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS solution.
    # Traverse tree recursively twice, once choosing left children first and once choosing right children first.
    # If tree is symmetric the outputs will be identical.
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def dfs(root: TreeNode, leftFirst: bool, res: list):
            res.append(root.val)

            if leftFirst:
                dfs(root.left, leftFirst, res) if root.left else res.append(None)
                dfs(root.right, leftFirst, res) if root.right else res.append(None)
            else:
                dfs(root.right, leftFirst, res) if root.right else res.append(None)
                dfs(root.left, leftFirst, res) if root.left else res.append(None)

        left = []
        right = []
        dfs(root, True, left)
        dfs(root, False, right)

        for l, r in zip(left, right):
            if l != r:
                return False

        return True


sol = Solution()
print(
    sol.isSymmetric(
        TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(3)),
        )
    )
)
print(
    sol.isSymmetric(
        TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    )
)
