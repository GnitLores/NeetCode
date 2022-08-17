class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # Solution using hashmap.
    # Use a dictionary to map old nodes to new nodes.
    # Once all the nodes are created, we can get the references from the dict.
    # O(n) time.
    def copyRandomList(self, head: Node) -> Node:
        hashmap = dict()
        hashmap[None] = None

        node = head
        while node:
            hashmap[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            newNode = hashmap[node]
            newNode.next = hashmap[node.next]
            newNode.random = hashmap[node.random]
            node = node.next

        return hashmap[head]

node4 = Node(1, None)
node3 = Node(10, node4)
node2 = Node(11, node3)
node1 = Node(13, node2)
node0 = Node(7, node1)

node4.random = None
node3.random = node2
node2.random = node4
node1.random = node0
node0.random = None

head = node0

sol = Solution()
res = sol.copyRandomList(head)
print("")