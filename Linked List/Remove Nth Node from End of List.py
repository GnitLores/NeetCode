# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Solution using two pointer with fixed offset n.
    # When fast ptr reach ends, slow pointer will be at node before node to delete.
    # Since we want to be at the node before the target node, start from a dummy node.
    # O(n) time and constant space.
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        fastPtr = dummy
        slowPtr = dummy
        cnt = 0
        while fastPtr:
            if cnt > n:
                slowPtr = slowPtr.next
            fastPtr = fastPtr.next
            cnt += 1
        
        if not slowPtr.next: # If the input was only one node
            return None
        else:
            slowPtr.next = slowPtr.next.next # Delete nth node from end
            head = dummy.next
            return head

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
    result = sol.removeNthFromEnd(sol, *args)
    if result:
        while result is not None:
            val = result.val
            print("val: " + str(val))
            result = result.next
    else:
        print(result)

testSolution(createNodes([1,2]), 2)
testSolution(createNodes([1,2,3,4,5]), 2)
testSolution(createNodes([1]), 1)
testSolution(createNodes([1,2]), 1)