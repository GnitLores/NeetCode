from CreateBinaryTree import *

class Solution:
    # Depth first search solution.
    # Since this is a binary search tree, we can skip searching the left subtree of a node
    # if it is below the min range since all subtree nodes will have lower values.
    # The same logic applies to the right subtree of a node that is greater than the max range.
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(root: TreeNode):
            res = root.val if low <= root.val <= high else 0
            if root.val >= low and root.left: res += dfs(root.left)
            if root.val <= high and root.right: res += dfs(root.right)
            return res
        return dfs(root)

sol = Solution()
print(sol.rangeSumBST(buildTree([10,5,15,3,7,None,18]), low = 7, high = 15))
print(sol.rangeSumBST(buildTree([10,5,15,3,7,13,18,1,None,6]), low = 6, high = 10))