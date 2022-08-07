class Solution(object):
    # Re use the solution from the Same Tree problem.
    # Recursive function that  checks if node is the same tree, and then checks if the subtree exists somewhere in the left and right subtrees.
    # O(n*m) time.
    def isSubtree(self, root, subRoot):
        if not root:
            if not subRoot:
                return True
            else:
                return False

        # Solution from Same Tree problem:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val: # Checking just for OR works because we already checked for AND case.
                    return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def hasSubtree(p, q):
            if p.val == subRoot.val:
                if isSameTree(p, q):
                    return True
            if p.left:
                if hasSubtree(p.left, q):
                    return True
            if p.right:
                if hasSubtree(p.right, q):
                    return True
            return False

        return hasSubtree(root, subRoot)


        

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
    result = sol.isSubtree(sol, *args)
    print(result)

tree = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subTree = TreeNode(4, TreeNode(1), TreeNode(2))
# printTree(tree1)
testSolution(tree, subTree)
tree = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subTree = TreeNode(4, TreeNode(2), TreeNode(1))
# printTree(tree1)
testSolution(tree, subTree)