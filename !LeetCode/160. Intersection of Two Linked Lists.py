# Definition for singly-linked list.
class ListNode:
    def __init__(self, x = 0, next = None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = set()

        while True:
            if headA:
                if headA in visited:
                    return headA
                else:
                    visited.add(headA)
                    headA = headA.next
            
            if headB:
                if headB in visited:
                    return headB
                else:
                    visited.add(headB)
                    headB = headB.next
            
            if not headA and not headB:
                break
            
        return None

sol = Solution()

intersect = ListNode(8, ListNode(4, ListNode(5)))
headA = ListNode(4, ListNode(1, intersect))
headB = ListNode(5, ListNode(6, ListNode(1, intersect)))
res = sol.getIntersectionNode(headA, headB)

headA = ListNode(4, ListNode(1))
headB = ListNode(5, ListNode(6, ListNode(1)))
res = sol.getIntersectionNode(headA, headB)