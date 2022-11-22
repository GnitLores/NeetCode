from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(nums):
    if not nums: return None
    numQ = deque(nums)
    root = TreeNode(numQ.popleft())
    nodeQ = deque([root])
    while numQ:
        node = nodeQ.popleft()

        node.left = TreeNode(numQ.popleft()) if numQ[0] else numQ.popleft()
        if node.left: nodeQ.append(node.left)
        if not numQ: break

        node.right = TreeNode(numQ.popleft()) if numQ[0] else numQ.popleft()
        if node.right: nodeQ.append(node.right)

    return root

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