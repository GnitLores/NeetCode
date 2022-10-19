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
    node = nodeQ.popleft()
    while numQ:
        node.left = TreeNode(numQ.popleft()) if numQ[0] else numQ.popleft()
        if node.left: nodeQ.append(node.left)
        if not numQ: break

        node.right = TreeNode(numQ.popleft()) if numQ[0] else numQ.popleft()
        if node.right: nodeQ.append(node.right)

        node = nodeQ.popleft()
    return root

class Solution:
    # Recursive solution. Get subtree strings and insert into node string with parenthesis.
    # If no nodes exist, just return node value string itself.
    # If only left node exist, ignore right node.
    # If only right node exist, include left node, but recursive function returns empty string if no node.
    # The string indicates preorder traversal node order.
    def tree2str(self, root: TreeNode) -> str:
        def dfs(root):
            if not root: return ""
            if not root.left and not root.right:
                return str(root.val)

            lStr = "".join(["(", dfs(root.left), ")"])
            
            if root.right:
                rStr = "".join(["(", dfs(root.right), ")"])
                return "".join([str(root.val), lStr, rStr])
            else:
                return "".join([str(root.val), lStr])
        res = dfs(root)
        return res

sol = Solution()
print(sol.tree2str(buildTree([1,2,3,4])))
print(sol.tree2str(buildTree([1,2,3,None,4])))
