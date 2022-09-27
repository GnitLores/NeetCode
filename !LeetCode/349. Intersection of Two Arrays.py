from typing import List


class Solution:
    # Solution using set intersection.
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = set(nums1), set(nums2)
        return nums1.intersection(nums2)

sol = Solution()
print(sol.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))