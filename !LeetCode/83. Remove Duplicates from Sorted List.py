# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
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
res = sol.deleteDuplicates(ListNode(1, ListNode(1, ListNode(1))))
print("")
res = sol.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2))))
print("")
res = sol.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))))
print("")