# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Observation: Every path must have a top node it passes through.
    # This means that we can simply visit every node and calculate the max path passing through it as top node.
    # This is the max sum when coming from the left and right subtrees plus the node value.
    # Since we need to know both the left and right subtree max at each node to calculate
    # the max path through that node, we need to do post-order traversal.
    # The we can then at each node record the global max sum.
    # If the max sum when coming from left or right subtree is negative, we can just set
    # it to zero instead, indicating the choice not to visit it.
    # The recursive function returns the max value visiting this node, which is then
    # the max of zero (not visiting), the node value plus left subtree max, and the node value
    # plus right subtree max.
    # O(n) time.
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = [-float("infinity")]

        def dfs(root: TreeNode):
            maxLeft = dfs(root.left) if root.left else 0
            maxRight = dfs(root.right) if root.right else 0

            rootSum = root.val + maxLeft + maxRight
            maxSum[0] = max(maxSum[0], rootSum)
            
            return max(0, root.val + maxLeft, root.val + maxRight)

        dfs(root)
        return maxSum[0]

sol = Solution()
print(sol.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))))
print(sol.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))