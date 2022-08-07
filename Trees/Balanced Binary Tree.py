class Solution(object):
    # Recursive postorder depth first search solution.
    # For each node, check if the subtrees are balanced.
    # Return node height.
    # O(n) time.
    def isBalanced(self, root):
        balanced = [True]

        def dfsIsBalanced(root):
            if root.left:
                leftHeight = dfsIsBalanced(root.left)
            else:
                leftHeight = 0
            if root.right:
                rightHeight = dfsIsBalanced(root.right)
            else:
                rightHeight = 0
            if abs(leftHeight - rightHeight) > 1:
                balanced[0] = False

            return max(leftHeight, rightHeight) + 1
        
        if root:
            dfsIsBalanced(root)
        return balanced[0]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Depth first search print:
def printTree(tree):
    print(tree.val)
    if tree.left: printTree(tree.left)
    if tree.right: printTree(tree.right)

def testSolution(*args):
    sol = Solution
    result = sol.isBalanced(sol, *args)
    print(result)

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15),TreeNode(7)))
# printTree(tree)
testSolution(tree)

tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
# printTree(tree)
testSolution(tree)