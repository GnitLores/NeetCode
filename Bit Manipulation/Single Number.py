class Solution(object):
    # Solution using bitwise xor operation.
    # The ordering in which we xor the numbers together does not matter xor does not matter.
    # Identical numbers cancel out, (1 xor 1 = 0) and (0 xor 0 = 0).
    # Only the ones of the individual number remain as ones.
    # O(n) time and constant extra space.
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res = n ^ res # bitwise xor
        return res

sol = Solution()
print(sol.singleNumber([2,2,1]))
print(sol.singleNumber([4,1,2,1,2]))
print(sol.singleNumber([1]))