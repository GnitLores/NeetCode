# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # It is possible to do this in place
    # using only constant extra space.
    # The code is quite complicated, but it is very efficient.
    # - Use slow and fast pointer technique to locate first node
    # of seconf half.
    # - From there, use slow pointer to reverse links in second half.
    # - Run through from both ends and check if palindrome.

    def isPalindrome(self, head: ListNode) -> bool:

        # Detect midpoint.
        # Slow pointer will end at first node of second half.
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # If list is too short to need reversing.
        if slow.next is None:
            return head.val == slow.val
        # Reverse the links of the second half with the slow pointer.
        prev = slow
        slow = slow.next
        prev.next = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            if nxt:
                slow = nxt
            else:
                break

        # Check if palindrome.
        # Check if values are the same and if the pointers reach the same node.
        # Check for same node after moving each pointer, because if the list is
        # even, they will end up next to each other and could otherwise skip past each other.
        while True:
            if head.val != slow.val:
                return False
            if head == slow:
                return True
            head = head.next
            if head == slow:
                return True
            slow = slow.next

    # Naive solution.
    # Just make an array, read all the values into it,
    # and check if it is a palindrom with two pointers.
    # Much simpler code but uses O(n) extra space and not
    # as efficient.
    def isPalindromeNaive(self, head: ListNode) -> bool:
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


sol = Solution()
print(sol.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))))
print(sol.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
print(sol.isPalindrome(ListNode(1, ListNode(2))))
print("")
print(
    sol.isPalindromeNaive(
        ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    )
)
print(sol.isPalindromeNaive(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
print(sol.isPalindromeNaive(ListNode(1, ListNode(2))))
