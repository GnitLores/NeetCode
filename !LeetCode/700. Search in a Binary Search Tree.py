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
    # In BST, in any node, smaller values are always in left subtree
    # and larger values in right subtree.
    # Search until node with target value is found, or an empty
    # child node is found.
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(root):
            if not root: return None
            if root.val == val: return root
            if root.val > val:
                return dfs(root.left)
            else:
                return dfs(root.right)
            
        return dfs(root)

sol = Solution()
res1 = sol.searchBST(root = buildTree([4,2,7,1,3]), val = 2)
res2 = sol.searchBST(root = buildTree([4,2,7,1,3]), val = 5)
pass