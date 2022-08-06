class Solution(object):
    # Recursive solution.
    # Recursively swap the subtrees of each node.
    # O(n) time and faster than 84.9% of solutions.
    def invertTree(self, root):
        if not root:
            return root
        if root.left or root.right:
            root.left, root.right = root.right, root.left
            root.left = self.invertTree(self, root.left)
            root.right = self.invertTree(self, root.right)
        return root

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
    result = sol.invertTree(sol, *args)
    printTree(result)

testSolution(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))))