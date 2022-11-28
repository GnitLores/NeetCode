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

        node.left = TreeNode(numQ.popleft()) if numQ[0] != None else numQ.popleft()
        if node.left: nodeQ.append(node.left)
        if numQ == None: break

        node.right = TreeNode(numQ.popleft()) if numQ[0] != None else numQ.popleft()
        if node.right: nodeQ.append(node.right)

    return root