# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS solution.
    # Pass through current sum and return true if leaf node with correct sum is found.
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        def dfs(root: TreeNode, sum):
            sum += root.val
            if not root.left and not root.right and sum == targetSum:
                return True
            if root.left and dfs(root.left, sum):
                return True
            return bool(root.right and dfs(root.right, sum))

        return dfs(root, 0)


sol = Solution()
print(sol.hasPathSum(TreeNode(1, TreeNode(2)), 1))
print(
    sol.hasPathSum(
        TreeNode(
            5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
        ),
        22,
    )
)
print(sol.hasPathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
print(sol.hasPathSum(None, 0))
