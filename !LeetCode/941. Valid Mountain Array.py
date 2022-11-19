from typing import List


class Solution:
    # It can be slightly complicated to check for the rising part because
    # any flat segment is always invalid, and a drop is valid if it is the peak.
    # One way to deal with this is to check for the following conditions for the array:
    # - It is long enough.
    # - It is never flat (rejects array with any segments that are not strictly increasing or decreasing).
    # - It starts out increasing (rejects strictly decreasing array).
    # - There is a peak where it drops (rejects stricly increasing array).
    # - It is strictly decreasing after that peak.
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        if arr[1] <= arr[0]: return False # Is array initially increasing?
        peakReached = False
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]: return False # Is array ever flat?
            if not peakReached and arr[i] < arr[i - 1]: peakReached = True # Detect peak
            if peakReached and arr[i] > arr[i - 1]: return False # Is array strictly decreasing after peak?
        return peakReached # Was peak found.
    
sol = Solution()
print(sol.validMountainArray(arr = [2,1]))
print(sol.validMountainArray(arr = [3,5,5]))
print(sol.validMountainArray([0,3,2,1]))