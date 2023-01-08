import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Since we're looking for the minimum height, it seems more efficient and simple to do a
    # BFS than a DFS. With a BFS we will always arrive at the min depth node before going to
    # a deeper level.
    # The BFS is done in rounds, incrementing the depth for each round.
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque()
        queue.append(root)

        level = 0
        while queue:
            level += 1
            for _ in range(len(queue)):
                node: TreeNode = queue.popleft()
                if (not node.left) and (not node.right):
                    return level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


sol = Solution()
print(sol.minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
print(sol.minDepth(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))
