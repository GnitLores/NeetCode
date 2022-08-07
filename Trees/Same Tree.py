class Solution(object):
    # Recursivively search through and check for mismatch.
    # O(n) time. Visits all nodes if trees are equal but breaks search when mismatch is found.
    def isSameTree(self, p, q):

        if (p is None) != (q is None): # xor
            return False
        if p is None and q is None:
            return True

        mismatchFound = [False]
        def findMismatch(p, q):
            if mismatchFound[0] == True: # Just stop recursion once mismatch is found.
                return

            if p.val != q.val:
                mismatchFound[0] = True
                return
            
            if (p.left is None) != (q.left is None): # xor
                mismatchFound[0] = True
                return

            if (p.right is None) != (q.right is None): # xor
                mismatchFound[0] = True
                return

            if p.left:
                findMismatch(p.left, q.left)
            if p.right:
                findMismatch(p.right, q.right)  
            return

        findMismatch(p, q)
        return not mismatchFound[0]

    # Simplified solution. Same time complexity and similar performance but simpler code.
    def isSameTreeSimple(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val: # Checking just for OR works because we already checked for AND case.
                return False

        return self.isSameTreeSimple(self, p.left, q.left) and self.isSameTreeSimple(self, p.right, q.right)



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
    result = sol.isSameTree(sol, *args)
    print(result)
    result = sol.isSameTreeSimple(sol, *args)
    print(result)

tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
# printTree(tree1)
testSolution(tree1, tree2)

tree1 = TreeNode(1, TreeNode(2))
tree2 = TreeNode(1, None, TreeNode(3))
# printTree(tree1)
testSolution(tree1, tree2)

tree1 = TreeNode(1, TreeNode(2), TreeNode(1))
tree1 = TreeNode(1, TreeNode(1), TreeNode(2))
# printTree(tree1)
testSolution(tree1, tree2)

testSolution(None, TreeNode(0))