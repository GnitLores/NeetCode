from CreateBinaryTree import *

class Solution:
    # Depth first search solution.
    # As long as node exists in both trees, sum the values and recursively continue.
    # If a node only exists in one tree, everything from that point is identical to
    # that tree.
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def dfs(root1: TreeNode, root2: TreeNode):
            if root1 and root2:
                root = TreeNode(root1.val + root2.val)
                root.left = dfs(root1.left, root2.left)
                root.right = dfs(root1.right, root2.right)
                return root
            else:
                return root1 or root2
        return dfs(root1, root2)

sol = Solution()
a = sol.mergeTrees(buildTree([1,3,2,5]), buildTree([2,1,3,None,4,None,7]))
b = sol.mergeTrees(buildTree([1]), buildTree([1,2]))
c = sol.mergeTrees(None, buildTree([1,2]))
d = sol.mergeTrees(buildTree([1,2]), None)
e = sol.mergeTrees(None, None)
f = sol.mergeTrees(buildTree([1,2,None,3]), buildTree([1,None,2,None,3]))
pass