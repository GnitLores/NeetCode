# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS solution. Return both the tiltsum and total sum of values in subtree with node as root.
    # The tiltsum is the tiltsum of the left plus right subtrees, plus the tilt
    # of the root node.
    # The tilt of the root node is the absolute difference between the sum of values
    # in left and right subtrees.
    def findTilt(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            if not root: return 0, 0

            tiltSumLeft, sumLeft = dfs(root.left)
            tiltSumRight, sumRight = dfs(root.right)

            tiltSum = tiltSumLeft + tiltSumRight + abs(sumLeft - sumRight)
            valSum = sumLeft + sumRight + root.val

            return tiltSum, valSum

        tiltSum, _ = dfs(root)
        return tiltSum

sol = Solution()
print(sol.findTilt(TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))))