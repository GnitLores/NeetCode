# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Even simpler solution using an outer scope variable
    # instead of passing back the sum.
    def sumOfLeftLeavesSimple(self, root: TreeNode) -> int:
        sum = [0]
        def dfs(root: TreeNode, isLeft: bool) -> int:
            if not root: return
            if isLeft and not root.left and not root.right:
                sum[0] += root.val
            dfs(root.left, True)
            dfs(root.right, False)
        dfs(root, False)
        return sum[0]


    # Depth first search.
    # Pass through left/right status of node from parent node.
    # Find sum for subtree if not leaf.
    # Return value if left leaf or return zero if right leaf.
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
print(sol.sumOfLeftLeavesSimple(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
print(sol.sumOfLeftLeavesSimple(TreeNode(1)))
print(sol.sumOfLeftLeavesSimple(None))
print("")
print(sol.sumOfLeftLeaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
print(sol.sumOfLeftLeaves(TreeNode(1)))
print(sol.sumOfLeftLeaves(None))