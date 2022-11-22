from typing import List


class Solution:
    # Given the constraints of the problem, only the element that
    # appears n times can be repeated and it must always be repeated.
    # We can detect repeated elements with a hashset.
    def repeatedNTimes(self, nums: List[int]) -> int:
        hashset = set()
        for n in nums:
            if n in hashset:
                return n
            else:
                hashset.add(n)

sol = Solution()
print(sol.repeatedNTimes(nums = [1,2,3,3]))
print(sol.repeatedNTimes(nums = [2,1,2,5,3,2]))
print(sol.repeatedNTimes(nums = [5,1,5,2,5,3,5,4]))