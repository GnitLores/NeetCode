# Definition for a binary tree node.
from typing import List
import math

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive pre order traversal solution.
    # Pass current max val along as argument and keep track of good nodes with outer scope variable.
    # O(n) speed.
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        
        def findGood(r, maxVal):
            if r.val >= maxVal:
                res.append(r.val)
                maxVal = r.val
                
            if r.left: findGood(r.left, maxVal)
            if r.right: findGood(r.right, maxVal)
            
        findGood(root, -math.inf)
        return len(res)

def testSolution(*args):
    sol = Solution
    result = sol.goodNodes(sol, *args)
    print(result)

tree = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
# printTree(tree)
testSolution(tree)