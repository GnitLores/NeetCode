# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def builList(nums):
    dummy = ListNode()
    node = dummy
    for n in nums:
        node.next = ListNode(n)
        node = node.next
    return dummy.next

class Solution:
    # Tortoise and hare algorithm.
    # Fast pointer travels twice as fast as slow pointer.
    # When fast pointer reaches end, slow pointer will be at middle.
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

sol = Solution()
a = sol.middleNode(builList([1,2,3,4,5]))
b = sol.middleNode(builList([1,2,3,4,5,6]))
pass