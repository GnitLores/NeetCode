# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Look through the nodes and sum the digits creating a new node.
    # Add carry to next node, or create an additional node if carry after last node.
    # O(n) time.
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        node = dummy
        carry = 0
        while l1 or l2:
            digit = carry
            carry = 0
            if l1:
                digit += l1.val
                l1 = l1.next
            if l2:
                digit += l2.val
                l2 = l2.next
            if digit > 9:
                carry = 1
                digit -= 10
            node.next = ListNode(digit)
            node = node.next
        if carry == 1:
            node.next = ListNode(1)

        return dummy.next

sol = Solution()

l1 = ListNode(2, ListNode(4, ListNode(3))) # [2,4,3]
l2 = ListNode(5, ListNode(6, ListNode(4))) # [5,6,4]
print(sol.addTwoNumbers(l1, l2)) # [7,0,8]: 342 + 465 = 807