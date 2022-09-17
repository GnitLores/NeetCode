# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Start from dummy node, and for each node, use inner loop to remove all target value nodes
    # until non target value node is found.
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        node = dummy
        while node:
            while node.next and node.next.val == val:
                node.next = node.next.next
            node = node.next
            
        return dummy.next

sol = Solution()
sol.removeElements(ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))), 6)
sol.removeElements(None, 1)
sol.removeElements(ListNode(7, ListNode(7, ListNode(7, ListNode(7)))), 7)