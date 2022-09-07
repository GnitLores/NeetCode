# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
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
print("")
print(sol.isPalindromeNaive(ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))))
print(sol.isPalindromeNaive(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
print(sol.isPalindromeNaive(ListNode(1, ListNode(2))))