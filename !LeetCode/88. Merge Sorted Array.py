from typing import List


class Solution:
    # Iterate backwards through arrays to avoid changing order.
    # Keep indices:
    # - Place insert at back of array 1
    # - Greatest uninserted value in array 1
    # - Greatest uninserted value in array 2
    # If both arrays have more values, insert greatest value first.
    # Otherwise insert from the one that does have more values.
    # Decrement indices while iterating backwards.
    # O(m + n)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        insertIndex = len(nums1) - 1
        idx1 = m - 1
        idx2 = n - 1
        while insertIndex >= 0:
            from1 = (
                idx1 >= 0
                and idx2 >= 0
                and nums1[idx1] > nums2[idx2]
                or idx1 >= 0
                and idx2 < 0
            )
            if from1:
                nums1[insertIndex] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[insertIndex] = nums2[idx2]
                idx2 -= 1
            insertIndex -= 1
        return


sol = Solution()
print(sol.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
print(sol.merge(nums1=[1], m=1, nums2=[], n=0))
print(sol.merge(nums1=[0], m=0, nums2=[1], n=1))
