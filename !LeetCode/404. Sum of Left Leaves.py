# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Depth first search.
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, isLeft: bool) -> int:
            if not root: return 0

            if not root.left and not root.right:
                if isLeft:
                    return root.val
                else:
                    return 0

            subtreeSum = 0
            subtreeSum += dfs(root.left, True)
            subtreeSum += dfs(root.right, False)
            return subtreeSum

        return dfs(root, False)

sol = Solution()
print(sol.sumOfLeftLeaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
print(sol.sumOfLeftLeaves(TreeNode(1)))
print(sol.sumOfLeftLeaves(None))