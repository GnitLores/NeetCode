# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Solution using queue.
    # For each level, add values of nodes in queue to output and add existing children to queue.
    # O(n) time.
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        res = []
        queue = [root]
        while queue:
            vals = []
            for _ in range(len(queue)):
                n = queue.pop(0)
                vals.append(n.val)
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)
            res.append(vals)

        return res

def testSolution(*args):
    sol = Solution
    result = sol.levelOrder(sol, *args)
    print(result)

tree = TreeNode(1, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# printTree(tree)
testSolution(tree)