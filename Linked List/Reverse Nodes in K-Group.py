# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Solution reusing function from Reverse Linked List problem.
    # Make a dummy node and designate it as the k-head node.
    # Search through and find the kth node following this.
    # Cut the link to the next node and store the reference.
    # Reverse the list linked to by the k-head node, and reinsert at
    # after the k-head.
    # Link the final node in the reversed group to the rest of the list,
    # and make it the current node and k-head.
    # O(n) time.
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        # Reverse list and return new head and tail
        def reverseList(head):
            previousNode = None
            node = head

            while node is not None:
                nextNode = node.next
                node.next = previousNode
                previousNode = node
                node = nextNode

            return previousNode, head # Old head is new tail

        dummy = ListNode()
        dummy.next = head
        node = dummy
        i = 0
        while node:
            # Set kHead to node before group to reverse
            if i == 0:
                kHead = node
            
            # Disconnect k group, reverse it, and reinsert it.
            # Set current node to final node of reversed group.
            if i == k:
                tmp = node.next
                node.next = None
                kHead.next, kTail = reverseList(kHead.next)
                kTail.next = tmp
                node = kTail
                i = 0
                continue
                
            node = node.next
            i += 1

        return dummy.next

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
    result = sol.reverseKGroup(sol, *args)
    print("")
    while result is not None:
        val = result.val
        print("val: " + str(val))
        result = result.next

testSolution(createNodes([1,2,3,4,5]), 2)
testSolution(createNodes([1,2,3,4,5]), 3)