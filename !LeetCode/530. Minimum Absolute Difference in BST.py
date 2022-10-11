# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Given the condition that this is a binary search tree,
    # for any given node, the smallest possible difference for that nodeis either
    # the difference between the node value and the greatest value in
    # the left subtree or the node value and the smallest value in the
    # right subtree.
    # This means that we can do a DFS returning the max and min values for
    # each node and check for a new min.
    def getMinimumDifference(self, root: TreeNode) -> int:
        minDif = [float('inf')]
        def dfs(root):
            if root.left:
                [leftSmall, leftBig] = dfs(root.left)
                minDif[0] = min(minDif[0], root.val - leftBig)
            else:
                leftSmall = root.val

            if root.right:
                [rightSmall, rightBig] = dfs(root.right)
                minDif[0] = min(minDif[0], rightSmall - root.val)
            else:
                rightBig = root.val
            
            return leftSmall, rightBig

        dfs(root)
        return minDif[0]

sol = Solution()
print(sol.getMinimumDifference(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))))
print(sol.getMinimumDifference(TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))))
print(sol.getMinimumDifference(TreeNode(236, TreeNode(104, None, TreeNode(227)), TreeNode(701, None, TreeNode(911)))))