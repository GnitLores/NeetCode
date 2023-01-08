# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Slightly simpler and more efficient solution.
    # No need to keep track of previous node, just jump
    # over equal value nodes in an inner loop.
    def deleteDuplicatesDoubleLoop(self, head: ListNode) -> ListNode:
        node = head
        while node:
            while node.next and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head

    # Keep track of previous node. If current node is equal to previous,
    # point from previous node directly to next relative to current node.
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        while node:
            if prev and node.val == prev.val:
                prev.next = node.next
            else:
                prev = node
            node = node.next

        return head


sol = Solution()
res = sol.deleteDuplicatesDoubleLoop(ListNode(1, ListNode(1, ListNode(1))))
print("")
res = sol.deleteDuplicatesDoubleLoop(ListNode(1, ListNode(1, ListNode(2))))
print("")
res = sol.deleteDuplicatesDoubleLoop(
    ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
)
print("")
res = sol.deleteDuplicates(ListNode(1, ListNode(1, ListNode(1))))
print("")
res = sol.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2))))
print("")
res = sol.deleteDuplicates(
    ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
)
print("")
