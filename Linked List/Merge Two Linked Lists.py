class Solution(object):
    # Merge two sorted linked lists.
    # Maintain a pointer to the current tail, and add the lowest node as the next.
    # O(n+m) time and faster than 91.6% of solutions.
    def mergeTwoLists(self, list1, list2):
        mergedList = ListNode() # start with a dummy node so that every node can be handled uniformly
        tail = mergedList # pointer to the current end of the merged list

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # Since the input lists are sorted, if they are not equally long, once one list is empty the other can just be appended.
        if list1 is not None:
            tail.next = list1
        if list2 is not None:
            tail.next = list2

        return mergedList.next # Don't return the dummy node

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

def testSolution(*args):
    sol = Solution
    result = sol.mergeTwoLists(sol, *args)
    while result is not None:
        val = result.val
        print("val: " + str(val))
        result = result.next

testSolution(createNodes([1,2,4]), createNodes([1,3,4]))