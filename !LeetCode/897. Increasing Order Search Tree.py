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
    # DFS solution using in-order traversal.
    # Maintain a pointer to the top node outside the dfs and during the dfs
    # track both the current node in the search tree and the current node in the output tree.
    # - Process the left subtree first, and unlink the left subtree.
    # - Add the current node in the search tree as a right child of the bottom node in the output tree
    # and make that the current output node.
    # - Process the right subtree.
    # After the dfs, return the top node.
    #
    # This works because in-order traversal processes the left subtree first, so we can unlink it safely.
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode, cur):
            if root.left:
                cur = dfs(root.left, cur)
                root.left = None
            cur.right = root
            cur = cur.right
            if root.right: cur = dfs(root.right, cur)
            return cur

        res = TreeNode()
        dfs(root, res)
        return res.right

sol = Solution()
a = sol.increasingBST(buildTree([5,3,6,2,4,None,8,1,None,None,None,7,9]))
b = sol.increasingBST(buildTree([5,1,7]))
pass