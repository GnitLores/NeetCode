# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    # Solution using hashset.
    # Vist one node from each list in each iteration.
    # Return the first node that gets visited twice.
    # Return null if both lists reach the end without repetition.
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = set()

        while True:
            if headA:
                if headA in visited:
                    return headA
                visited.add(headA)
                headA = headA.next

            if headB:
                if headB in visited:
                    return headB
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
