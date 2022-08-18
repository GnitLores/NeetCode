# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Solution using recursive traversal.
    # Recursively check if subtrees are BSTs and return min and max subtree values.
    # O(n) time, visits each node once.
    def isValidBST(self, root: TreeNode) -> bool:

        def searchTree(root):
            isBST = True
            minVal = root.val
            maxVal = root.val
            
            if root.left:
                [leftIsBST, leftMin, leftMax] = searchTree(root.left)
                isBST = isBST and leftIsBST and leftMax < root.val
                minVal = min(minVal, leftMin)
                maxVal = max(maxVal, leftMax)

            if root.right:
                [rightIsBST, rightMin, rightMax] = searchTree(root.right)
                isBST = isBST and rightIsBST and rightMin > root.val
                minVal = min(minVal, rightMin)
                maxVal = max(maxVal, rightMax)

            return [isBST, minVal, maxVal]

        [isBST, _, _] = searchTree(root)

        return isBST

    # Solution based on limits.
    # Recursively traverse and check the value of nodes against the limits of
    # what it can be without violating BST.
    # O(n) time.
    def isValidBSTLimits(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))

sol = Solution()
print(sol.isValidBST(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(6), TreeNode(9)))))
print(sol.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))))
print(sol.isValidBSTLimits(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(6), TreeNode(9)))))
print(sol.isValidBSTLimits(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))))