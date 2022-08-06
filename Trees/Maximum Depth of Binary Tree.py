class Solution(object):
    # Recursive solution.
    # Search each subtree for max depth and return max.
    # If bottom node, return node depth.
    # Could also have been solved iteratively with a queue or stack.
    # O(n) speed and faster than 81.6% of solutions.
    def maxDepth(self, root):
        if not root:
            return 0
        maxDepth = self.searchDepth(self, root, 0)

        return maxDepth

    def searchDepth(self, root, depth):
        depth += 1
        maxDepth = depth
        if root.left:
            maxDepth = max(self.searchDepth(self, root.left, depth), maxDepth)
        if root.right:
            maxDepth = max(self.searchDepth(self, root.right, depth), maxDepth)
        return maxDepth

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
    result = sol.maxDepth(sol, *args)
    print(result)

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# printTree(tree)
testSolution(tree)
