from typing import List
from CreateBinaryTree import *

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