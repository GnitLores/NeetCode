from typing import List


class Solution:
    # Solution using formula for sum from 1 to n.
    # Just subtract this from the sum of nums.
    # O(n) if calculating max of array is O(n).
    # We could also just have summed up 1 to n.
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        return sum(nums) - (n*(n+1))//2

    # Could also have been solved using floyd's tortoise and hare algorithm.
    # Treat array as a linked list with each number pointing to the index of the next number.
    # This works because the numbers are <= the length of the array.
    # A number appearing twice means that two numbers point to the same element.
    # In other words, this is the beginning of a cycle in the linked list.
    # Floyd:
    # Start fast and slow pointer at element 0.
    # Iterate until they meet in the cycle.
    # Now start slow pointer from both the first element and the meeting point in the cycle.
    # The slow pointers will always meet at the start of the cycle.
    # O(n) time.
    def findDuplicateFloyd(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

sol = Solution()
print(sol.findDuplicate([1,3,4,2,2]))
print(sol.findDuplicate([3,1,3,4,2]))
print("")
print(sol.findDuplicateFloyd([1,3,4,2,2]))
print(sol.findDuplicateFloyd([3,1,3,4,2]))