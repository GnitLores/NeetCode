from typing import Optional
from CreateBinaryTree import *

class Solution:
    # Depth first solution.
    # Use root value as reference value and check all nodes against it until
    # a mismatch is is found.
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        refVal = root.val
        def dfs(root: TreeNode):
            if root.val != refVal: return False
            if root.left and not dfs(root.left): return False
            if root.right and not dfs(root.right): return False
            return True
        return dfs(root)

sol = Solution()
print(sol.isUnivalTree(buildTree([1,1,1,1,1,None,1])))
print(sol.isUnivalTree(buildTree([2,2,2,5,2])))
print(sol.isUnivalTree(buildTree([1,1])))