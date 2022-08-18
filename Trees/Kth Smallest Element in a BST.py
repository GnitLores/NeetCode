# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Solution using recursive in order traversal.
    # In a BST, in order traversal visits nodes in ascending order.
    # Simply count each visit and record the value at the kth visit.
    # Coul also have added return statements when k > visit to optimize, but it's not necessary.
    # O(n) time and O(1) extra space.
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        val = [None]

        def countInOrder(root, visit):
            if root.left:
                visit = countInOrder(root.left, visit)

            visit += 1
            if visit == k:
                val[0] = root.val

            if root.right:
                visit = countInOrder(root.right, visit)

            return visit
            
        countInOrder(root, 0)
        return val[0]

    # Solution using stack to traverse iteratively in order.
    # Every time a null is encountered, pop a node and "visit" it.
    # O(n) time and might be O(logn) extra space.
    def kthSmallestStack(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

sol = Solution()
print(sol.kthSmallest(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(6), TreeNode(9))), 1))
print(sol.kthSmallest(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(6), TreeNode(9))), 2))
print(sol.kthSmallest(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(6), TreeNode(9))), 3))
print(sol.kthSmallest(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(6), TreeNode(9))), 4))
print(sol.kthSmallest(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(6), TreeNode(9))), 5))
print("")
print(sol.kthSmallestStack(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(6), TreeNode(9))), 1))
print(sol.kthSmallestStack(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(6), TreeNode(9))), 2))
print(sol.kthSmallestStack(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(6), TreeNode(9))), 3))
print(sol.kthSmallestStack(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(6), TreeNode(9))), 4))
print(sol.kthSmallestStack(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(6), TreeNode(9))), 5))