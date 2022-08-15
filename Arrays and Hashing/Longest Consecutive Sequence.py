class Solution(object):
    # Solution using hashset.
    # The key is that if all the numbers are added to a set,
    # it can be verified if a number n can start a sequence
    # by testing if n-1 is in the set.
    # If something starts a sequence, see how many subsequent numbers
    # are also in the set.
    # O(n) time.
    def longestConsecutive(self, nums):
        numSet = set(nums)
        maxSeq = 0
        for n in nums:
            if n-1 not in numSet:
                length = 1
                while n+length in numSet:
                    length += 1
                maxSeq = max(maxSeq, length)
        return maxSeq

sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))