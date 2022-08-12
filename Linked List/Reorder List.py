# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # Solution using array.
    # Add all nodes to array.
    # Use two pointers at beginning and end of array.
    # Reassemble list by iterating from both ends of array.
    # O(n) time.
    def reorderList(self, head: ListNode) -> None:
        queue = []
        node = head
        while node:
            queue.append(node)
            node = node.next
            queue[-1].next = None
        
        dummy = ListNode()
        node = dummy
        l = 0
        r = len(queue) - 1
        while l <= r:
            node.next = queue[l]            
            node = node.next
            l += 1
            if r > l:
                node.next = queue[r]            
                node = node.next
                r -= 1
        head = dummy.next
    
    # Solution reordering in place.
    # More complicated, but not extra space.
    # Find midpoint using tortoise and hare pointers.
    # Reverse the second half of the list using solution from Reverse Linked List problem.
    # Weave nodes from reversed second half in between nodes of first half.
    # Also O(n) time, but constant space.
    def reorderListInPlace(self, head: ListNode) -> None:
        def reverseList(h):
            prev = None
            n = h
            while n is not None:
                next = n.next
                n.next = prev
                prev = n
                n = next
            return prev

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        head2 = reverseList(head2)
        
        node = head
        node2 = head2
        while node:
            if node2:
                link = node.next
                node.next = node2
                node2 = node2.next
                node.next.next = link
                node = node.next.next
            else:
                node = node.next

# Create list nodes for problem:
def createNodes(values):
    if len(values) > 1:
        nextNode = createNodes(values[1:])
    else:
        nextNode = None
    node = ListNode(values[0], nextNode)
    return node

def testSolution(*args):
    sol = Solution
    sol.reorderList(sol, createNodes(*args))
    sol = Solution
    sol.reorderListInPlace(sol, createNodes(*args))

# testSolution([1,2,3,4])
testSolution([1,2,3,4,5])