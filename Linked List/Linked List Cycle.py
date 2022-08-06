class Solution(object):
    # Add nodes to hashset and check if node has already been passed.
    # O(n) time and faster than 59.8% of solutions.
    def hasCycle(self, head):
        hashset = set()
        node = head
        while node:
            if node in hashset:
                return True
            hashset.add(node)
            node = node.next
        return False

    # Using the Tortoise and Hare solution:
    # Pointers are guaranteed to meet in O(n) time if there is a loop since the distance between them decreases by 1 per iteration.
    # O(n) time and O(1) space.
    def hasCycleTortoiseHare(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create list nodes for problem:
def createNodes(values):
    if len(values) > 1:
        nextNode = createNodes(values[1:])
    else:
        nextNode = None
    node = ListNode(values[0], nextNode)
    return node

def createCycle(list, cyclePos):
    node = list
    while node:
        if cyclePos == 0:
            cyclePointer = node
        cyclePos -= 1

        if node.next is None:
            node.next = cyclePointer
            break
        else:
            node = node.next
    return list
    

def testSolution(*args):
    sol = Solution
    result = sol.hasCycle(sol, *args)
    print("Hashing: " + str(result))
    result = sol.hasCycleTortoiseHare(sol, *args)
    print("Tortoise and Hare: " + str(result))


testSolution(createCycle(createNodes([3,2,0,4]), 1))
testSolution(createCycle(createNodes([1,2]), 0))
testSolution(createNodes([1]))