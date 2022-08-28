from statistics import median
from typing import List


class Solution:
    # Solution using binary search.
    # Observation: Since the median is the middle value, we know just from the total size
    # of the arrays how many elements will be to the left and right of it in total.
    # That means that if we choose to partition one of the arrays at a certain place,
    # then we already know where to partition the other array to get the correct total partition size.
    # This means that we can just do a binary search for the correct partition point in one array,
    # calculating the corresponding partition point in the other array, and checking if we have found
    # a valid median.
    # Since both arrays are ordered, at the correct partition point at the median value, the rightmost
    # element of the left partition of one array must be <= the leftmost element of the right partition
    # of the other array. This must be true for both arrays.
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
         # Always start with midpoint of smaller array
         # This prevents several complications, for example when one array is empty
        if len(B) < len(A):
            A, B = B, A
        
        inf = float("inf") # Use inf for comparisons
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # Midpoint of A
            j = half - i - 2 # Number of element to include from B for correct partition size. -2 because both arrays are zero indexed.

            # Partition arrays, default to inf if partition point moves OOB
            Aleft = A[i] if i >= 0 else -inf             # Rightmost element of left partition of A
            Aright = A[i + 1] if i + 1 < len(A) else inf # Leftmost element of right partition of A
            Bleft = B[j] if j >= 0 else -inf             # Rightmost element of left partition of B
            Bright = B[j + 1] if j + 1 < len(B) else inf # Leftmost element of right partition of B

            if Aleft <= Bright and Bleft <= Aright: # If correct partition:
                if total % 2 == 1:  # If odd
                    return min(Aright, Bright) # Return middle element
                else:               # If even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 # Return average of two middle elements
            # If we didn't find median, halve the size of the binary search boundaries of array A:
            elif Aleft > Bright: # Too many elements from A
                r = i - 1 # reduce partition size of A
            else: # Not enough elements from A
                l = i + 1 # Increase partition size of A

sol = Solution()
print(sol.findMedianSortedArrays(nums1 = [1,3,5,7,9], nums2 = [2,4,6,8,10,11,12,13,14,15,16]))
print(sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
print(sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))