class Solution(object):
    # In a binary search tree, smaller values are in left subtree, and greater values are in right subtree.
    # Hence, if both target nodes have smaller or greater values, they must both be in the left or right subtress.
    # In that case there is a lower common ancestor in that subtree.
    # Search until one target is greater and the other is smaller, or the node itself is a target.
    # O(logn) time.
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if (p.val < root.val) and (q.val < root.val):
                root = root.left
            elif (p.val > root.val) and (q.val > root.val):
                root = root.right
            else:
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
    result = sol.lowestCommonAncestor(sol, *args)
    print(result.val)

tree = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
node1 = TreeNode(2)
node2 = TreeNode(8)
#printTree(tree)
testSolution(tree, node1, node2)

tree = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
node1 = TreeNode(2)
node2 = TreeNode(4)
#printTree(tree)
testSolution(tree, node1, node2)

tree = TreeNode(2, TreeNode(1), None)
node1 = TreeNode(2)
node2 = TreeNode(1)
#printTree(tree)
testSolution(tree, node1, node2)

tree = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
node1 = TreeNode(1)
node2 = TreeNode(4)
#printTree(tree)
testSolution(tree, node1, node2)