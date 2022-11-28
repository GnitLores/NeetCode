# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive solution based on these observations:
    # Preorder traversal: The first visited node is the root. Left subtree nodes are all visited before right subtree nodes.
    # Inorder traversal: Every node in the left subtree is visited before the root, every node in the right after.
    # Values are unique.
    # Conclusion, the first value in the preorder list gives the midpoint in the inorder list.
    # The number of elements to the left in the inorder list is the number of elements after the root
    # that are in the left subtree in the preorder list.
    # We can use this to split the lists into left and right and recursively build the tree.
    # O(n) time as each node is visited once.
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0: return None

        rootVal = preorder.pop(0)
        if len(preorder) == 0: return TreeNode(rootVal)

        leftPreorder = []
        leftInorder = []
        while inorder[0] != rootVal:
            leftInorder.append(inorder.pop(0))
            leftPreorder.append(preorder.pop(0))
        else:
            inorder.pop(0)

        root = TreeNode(rootVal)
        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(preorder, inorder)

        return root
    
    # Same exact method, but using indexing instead of popping to new lists.
    # Same time complexity but simpler code and more efficient.
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root

sol = Solution()
test1 = sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
test2 = sol.buildTree([1,2,4,5,3], [4,2,5,1,3])
print("")