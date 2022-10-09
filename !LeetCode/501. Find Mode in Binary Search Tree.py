import collections
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS counting elements and keeping track of max count.
    # To do this with constant space it would probably be necessary to
    # search through the tree twice - once to find the max count
    # and once to find values that occur that number of times.
    def findMode(self, root: TreeNode) -> List[int]:
        count = collections.defaultdict(int)
        res = []
        maxCount = [0]

        def dfs(root: TreeNode):
            count[root.val] += 1
            cnt = count[root.val]
            if  cnt == maxCount[0]:
                res.append(root.val)
            if cnt > maxCount[0]:
                res.clear()
                res.append(root.val)
                maxCount[0] = cnt

            if root.left: dfs(root.left)
            if root.right: dfs(root.right)

        dfs(root)
        return res

sol = Solution()
print(sol.findMode(TreeNode(1, TreeNode(1), TreeNode(2, TreeNode(2)))))
print(sol.findMode(TreeNode(1, None, TreeNode(2, TreeNode(2)))))
print(sol.findMode(TreeNode(0)))