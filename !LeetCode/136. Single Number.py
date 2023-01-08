import collections
from typing import List


class Solution:
    # Bit manipulation solution.
    # The order in which you xor a list of numbers does not change result.
    # Using xor on two identical numbers gives 0
    # Using xor on 0 and a number gives the number unchanged.
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        return res

    # Solution using a hashset.
    # Add each number to a hashset and remove it when second instance is found.
    # Return only remaining number.
    def singleNumberHashset(self, nums: List[int]) -> int:
        hashset = set()
        for n in nums:
            hashset.remove(n) if n in hashset else hashset.add(n)
        return hashset.pop()

    # Solution using hashmap to count numbers.
    # Requires iterating twice.
    def singleNumberCount(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
        for n in nums:
            if count[n] == 1:
                return n


sol = Solution()
print(sol.singleNumber([2, 2, 1]))
print(sol.singleNumber([4, 1, 2, 1, 2]))
print(sol.singleNumber([1]))
print("")
print(sol.singleNumberHashset([2, 2, 1]))
print(sol.singleNumberHashset([4, 1, 2, 1, 2]))
print(sol.singleNumberHashset([1]))
print("")
print(sol.singleNumberCount([2, 2, 1]))
print(sol.singleNumberCount([4, 1, 2, 1, 2]))
print(sol.singleNumberCount([1]))
