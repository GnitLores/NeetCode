from typing import List


class Solution:
    # We can track the greatest and second greatest values.
    # When a new greatest value is found, the previous greatest becomes
    # the second greatest, and the index is recorded.
    #
    # If we didn't need to return the index it would be simpler to just
    # create a max heap and use the two top values.
    def dominantIndex(self, nums: List[int]) -> int:
        first, second, idx = -1, -1, None
        for i, n in enumerate(nums):
            if n > first:
                second = first
                first = n
                idx = i
            elif n > second:
                second = n

        if first >= 2 * second:
            return idx
        else:
            return -1

sol = Solution()
print(sol.dominantIndex(nums = [3,6,1,0]))
print(sol.dominantIndex(nums = [1,2,3,4]))
print(sol.dominantIndex(nums = [0,0,0,1]))