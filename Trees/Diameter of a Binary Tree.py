class Solution(object):
    # Recursive postorder traversal solution.
    # For each node, check the max path with this node as root and update global max path.
    # Return height of node.
    # O(n) time.
    def diameterOfBinaryTree(self, root):
        maxPath = [0] # Lists can be accessed in outer scope. Making this an int would require nonlocal keyword which doesn't work on leetcode.
        def searchMaxPathLength(root):

            if root.left:
                maxLeftPath = searchMaxPathLength(root.left) + 1
            else:
                maxLeftPath = 0
            if root.right:
                maxRightPath  = searchMaxPathLength(root.right) + 1
            else:
                maxRightPath = 0
            
            maxPath[0] = max(maxPath[0], maxLeftPath + maxRightPath)
            return max(maxLeftPath, maxRightPath)

        searchMaxPathLength(root)
        return maxPath[0]

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
    result = sol.diameterOfBinaryTree(sol, *args)
    print(result)

tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),TreeNode(3))
# printTree(tree)
testSolution(tree)

tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), None)
# printTree(tree)
testSolution(tree)