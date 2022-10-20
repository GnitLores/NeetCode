# Definition for a binary tree node.
from collections import deque
from typing import List

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
    # Breadth first search done in rounds using queue.
    # Process all nodes in a layer, adding all child nodes to the queue.
    # Then process all the added nodes in the same way.
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = deque([root])
        res = []
        while q:
            levelSum = 0
            layerNodes = len(q)
            for _ in range(layerNodes):
                node = q.popleft()
                levelSum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(levelSum / layerNodes)
        return res

sol  = Solution()
print(sol.averageOfLevels(buildTree([3,9,20,None,None,15,7])))
print(sol.averageOfLevels(buildTree([3,9,20,15,7])))
print(sol.averageOfLevels(buildTree([1])))