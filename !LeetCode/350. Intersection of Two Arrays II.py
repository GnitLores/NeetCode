import collections
from typing import List


class Solution:
    # Solution using dictionary.
    # Count numbers in one array, and iterate through the other, adding shared
    # numbers and decrementing count.
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = collections.defaultdict(int)
        for n in nums1:
            count1[n] += 1
        res = []
        for n in nums2:
            if count1[n] > 0:
                res.append(n)
                count1[n] -= 1
        return res

    # Solution using two dictionaries.
    # Count both arrays and add minimum count to output.
    # A bit less efficient.
    def intersectTwoDicts(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)
        for n in nums1:
            count1[n] += 1
        for n in nums2:
            count2[n] += 1
        res = []
        for n in count1.keys():
            for _ in range(min(count1[n], count2[n])):
                res.append(n)

        return res

sol = Solution()
print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
print(sol.intersectTwoDicts(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol.intersectTwoDicts(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))