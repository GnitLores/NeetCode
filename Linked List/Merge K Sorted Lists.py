# Definition for singly-linked list.
from typing import List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Solution using minheap.
    # Keep a minheap with exactly one node from each list ordered by the value and with listNr.
    # Every time we pop a node from the heap, push a node from the same list unto the heap.
    # Continue poppung from heap and linking in output list until no more nodes remain.
    # O(n*logk) time, where k is the number of lists.
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not any(lists): return None
        heap = []
        cnt = [0] 

        # Push the next node from a specific list on the heap.
        def addToheap(listNr):
            head = lists[listNr]
            if not head: return

            node = head
            lists[listNr] = head.next
            node.next = None
            val = node.val
            # If multiple instances of the same value exists, the next element of the tuple will be compared.
            # The purpose of the count here is to distinguish nodes with the same value from the same list.
            # Without a unique count, we could have node references being compared which will return an error.
            heapq.heappush(heap, (val, cnt[0], listNr, node))

            cnt[0] += 1
        
        # Pop the node with minimal value and push next node from the same list.
        def popFromHeap():
            _, _, listNr, node = heapq.heappop(heap)
            addToheap(listNr)
            return node

        # Initialize heap
        for i, _ in enumerate(lists):
            addToheap(i)

        # Merge all nodes
        head = popFromHeap()
        tail = head
        while heap:
            tail.next = popFromHeap()
            tail = tail.next

        return head

    # Neetcode solution.
    # We could also have reused the solution from the Merge Two Linked Lists problem.
    # Merging two lists is O(n), and if we merge pairs of lists and then merge the
    # resulting lists until only one remains, we have to merge logk times.
    # O(n*logk) time.
    def mergeKListsNoHeap(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

sol = Solution()
res = sol.mergeKLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
while res:
    print(res.val)
    res = res.next

print("")
res = sol.mergeKListsNoHeap([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
while res:
    print(res.val)
    res = res.next