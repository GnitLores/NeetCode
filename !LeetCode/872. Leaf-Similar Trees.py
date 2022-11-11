from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(nums):
    if not nums: return None
    numQ = deque(nums)
    root = TreeNode(numQ.popleft())
    nodeQ = deque([root])
    while numQ:
        node = nodeQ.popleft()

        node.left = TreeNode(numQ.popleft()) if numQ[0] else numQ.popleft()
        if node.left: nodeQ.append(node.left)
        if not numQ: break

        node.right = TreeNode(numQ.popleft()) if numQ[0] else numQ.popleft()
        if node.right: nodeQ.append(node.right)

    return root


class Solution:
    # DFS solution.
    # Pass through reference to list and append node value when reaching leaf node.
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root, leaves: list):
            if not root.left and not root.right:
                leaves.append(root.val)
            else:
                if root.left: leaves = dfs(root.left, leaves)
                if root.right: leaves = dfs(root.right, leaves)
            return leaves

        return dfs(root1, []) == dfs(root2, [])

sol = Solution()
print(sol.leafSimilar(buildTree([3,5,1,6,2,9,8,None,None,7,4]), buildTree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])))
print(sol.leafSimilar(buildTree([1,2,3]), buildTree([1,3,2])))