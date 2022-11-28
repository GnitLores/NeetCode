from CreateBinaryTree import *

class Solution:
    # Breadth first search solution using hashset. Similar to normal two sum solution but using
    # BFS to scan through values.
    def findTarget(self, root: TreeNode, k: int) -> bool:
        q = deque([root])
        hashset = set()
        while q:
            node = q.popleft()
            if k - node.val in hashset: return True
            hashset.add(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        return False

sol = Solution()
print(sol.findTarget(root = buildTree([5,3,6,2,4,None,7]), k = 9))
print(sol.findTarget(root = buildTree([5,3,6,2,4,None,7]), k = 28))