from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return

        insertIndex = len(nums1) - 1
        idx1 = m - 1
        idx2 = n - 1
        while insertIndex >= 0:
            if idx1 < 0:
                from1 = False
            elif idx2 < 0:
                from1 = True
            else:
                if nums1[idx1] > nums2[idx2]:
                    from1 = True
                else:
                    from1 = False

            if from1:
                nums1[insertIndex] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[insertIndex] = nums2[idx2]
                idx2 -= 1
            insertIndex -= 1
        return
            
        
sol = Solution()
print(sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(sol.merge(nums1 = [1], m = 1, nums2 = [], n = 0))
print(sol.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))