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
    # Since min values propagate up through the tree due to the special property,
    # we know that the root must have the min value.
    # However this is not necessarily the case for the second smallest value.
    # It can be located deep in the tree if it ever matches up with the min value.
    # Thus we have to search through the tree for the minimum value which is greater
    # than the root value.
    # We also know that if a node has a greater value than the current second minimum,
    # the second minimum cannot possibly be located in the subtree, otherwise it would
    # have propagated and become the node value. Thus we can break off the search for
    # the subtree at that point.
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, second):
            if node.val > root.val:
                second = min(second, node.val)
            
            if node.left and node.left.val < second:
                second = min(second, dfs(node.left, second))
            if node.right and node.right.val < second:
                second = min(second, dfs(node.right, second))
            return second
        
        referenceMin = float("inf")
        second = dfs(root, referenceMin)
        if second == referenceMin: return -1
        return second

        

sol = Solution()
print(sol.findSecondMinimumValue(buildTree([2,2,5,None,None,5,7])))
print(sol.findSecondMinimumValue(buildTree([2,2,2])))
print(sol.findSecondMinimumValue(buildTree([1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1])))