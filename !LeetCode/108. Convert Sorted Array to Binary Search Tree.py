from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def createTree(l, r):
            if l > r: return None
            if l == r: return TreeNode(nums[l])
            m = (l + r) // 2
            return TreeNode(nums[m], createTree(l, m - 1), createTree(m + 1, r))

        return createTree(0, len(nums) - 1)

sol = Solution()
res = sol.sortedArrayToBST([-10,-3,0,5,9])
print("")
res = sol.sortedArrayToBST([1,3])
print("")