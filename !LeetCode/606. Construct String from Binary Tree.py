from CreateBinaryTree import *

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
