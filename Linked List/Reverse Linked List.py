# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative solution. Loop through and link to previous node.
# O(n) time, faster than 72.1 of solutions.
class Solution(object):
    def reverseList(self, head):

        previousNode = None
        node = head

        while node is not None:
            nextNode = node.next
            node.next = previousNode
            previousNode = node
            node = nextNode

        return previousNode

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
    result = sol.reverseList(sol, *args)
    while result is not None:
        val = result.val
        print("val: " + str(val))
        result = result.next

testSolution(createNodes([1,2,3,4,5]))