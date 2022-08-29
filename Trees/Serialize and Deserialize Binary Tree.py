# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Codec:
    # Solution using preorder DFS traversal.
    # Numbers encoded reusing Encode and Decode Strings problem solution with # delimiter.
    # Left and right node encoded as "L" and "R".
    # Return encoded as "ø".
    # Decoding starts from dummy root to keep things consistent.
    def serialize(self, root):
        if not root: return ""
        res = ["L"]
        
        def dfs(root: TreeNode):
            s = str(root.val)
            
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
            if root.left:
                res.append("L")
                dfs(root.left)
            if root.right:
                res.append("R")
                dfs(root.right)
            res.append("ø")

        dfs(root)
        res.append("ø")
        return "".join(res)
        

    def deserialize(self, data):
        if data == "": return []
        dummy = TreeNode(0)

        def readVal(i):
            j = i + 1
            while data[j] != "#":
                j += 1
            chars = int(data[i + 1:j])
            val = int(data[j + 1:j + 1 + chars])
            dir = data[i]
            i = j + 1 + chars
            return val, dir, i

        def dfs(root, i):
            while data[i] != "ø":
                val, dir, i = readVal(i)

                if dir == "L":
                    root.left = TreeNode(val)
                    i = dfs(root.left, i)
                elif dir == "R":
                    root.right = TreeNode(val)
                    i = dfs(root.right, i)
            return i + 1

        dfs(dummy, 0)
        return dummy.left
    
    # Neetcode solution.
    # They also used preorder DFS traversal.
    # Very simple, just comma separated numbers indicating values, and "N" indicating no node.
    # This means if a node has no children, two "N"s will occur. 
    def serializeSimple(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserializeSimple(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

codec = Codec()
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
s = codec.serialize(root)
res = codec.deserialize(s)

s = codec.serializeSimple(root)
res = codec.deserializeSimple(s)