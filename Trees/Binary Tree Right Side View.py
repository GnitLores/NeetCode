# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Solution using level order traversal with queue.
    # For each level, store the value of the last node in the level.
    # O(n) time.
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            rightVal = None
            for _ in range(len(queue)):
                n = queue.pop(0)
                rightVal = n.val
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)

            res.append(rightVal)
        return res

def testSolution(*args):
    sol = Solution
    result = sol.rightSideView(sol, *args)
    print(result)

tree = TreeNode(1, TreeNode(2, None, TreeNode(5, None, TreeNode(7))), TreeNode(3, None, TreeNode(4)))
testSolution(tree)