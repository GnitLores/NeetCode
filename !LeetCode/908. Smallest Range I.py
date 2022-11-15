from typing import List


class Solution:
    # The final score will always depend only on the max and min elements of the array because any
    # values smaller than the max can also produce values at least as close to the min element and
    # vice versa.
    # Find the smallest possible value of the max element (subtracting k) and
    # find the largest possible value of the min element (adding k).
    # If those do not overlap, the score is the size of the gap bewteen them.
    # If they do overlap, the score is 0 because we can produce two identical value in some way.
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        largestMin = min(nums) + k
        smallestMax = max(nums) - k
        smallestDifference = smallestMax - largestMin
        return max(0, smallestDifference)

sol = Solution()
print(sol.smallestRangeI(nums = [1,5,9,74,77], k = 2))
print(sol.smallestRangeI(nums = [1], k = 0))
print(sol.smallestRangeI(nums = [0,10], k = 2))
print(sol.smallestRangeI(nums = [1,3,6], k = 3))