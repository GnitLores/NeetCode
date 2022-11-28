from CreateBinaryTree import *

class Solution:
    # DFS solution.
    # In a binary search tree, we can traverse through all elements in ascending order
    # using in order traversal (visit left subtree -> node -> right subtre).
    # We just need to keep track of the previous node value and update the min difference.
    def minDiffInBST(self, root: TreeNode) -> int:
        prevVal = [None]
        minDif = [float("inf")]
        def dfs(root: TreeNode):
            if root.left: dfs(root.left)
            if prevVal[0] != None:
                minDif[0] = min(minDif[0], abs(prevVal[0] - root.val))
            prevVal[0] = root.val
            if root.right: dfs(root.right)

        dfs(root)
        return minDif[0]

sol = Solution()
print(sol.minDiffInBST(buildTree([4,2,6,1,3])))
# print(sol.minDiffInBST(buildTree([1,0,48,None,None,12,49])))