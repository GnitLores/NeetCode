from typing import List


class Solution:
    # We know that the total sum of the array must be divisible by 3 and
    # that the target sum of each part must be an integer derived by
    # that division.
    # We can then calculate a running sum searching through the array
    # and creating a partition whenever the sum is equal to the target,
    # and reset the current running sum.
    # The main problem is that some sequences may sum to zero.
    # We just need to ensure that there are 3 partitions that sum
    # to the target sum, and that either those partitions constitute
    # the entire array or that the remainder of the array sums to zero.
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0: return False
        target = total // 3
  
        part = 0
        cur = 0
        for i, n in enumerate(arr):
            cur += n
            if cur == target:
                part += 1
                cur = 0
            if part == 3:
                break
        if part < 3: return False
        if i < len(arr) - 1:
            return sum(arr[i + 1:]) == 0
        return True

sol = Solution()
print(sol.canThreePartsEqualSum(arr = [0,2,1,-6,6,-7,9,1,2,0,1]))
print(sol.canThreePartsEqualSum(arr = [0,2,1,-6,6,7,9,-1,2,0,1]))
print(sol.canThreePartsEqualSum(arr = [3,3,6,5,-2,2,5,1,-9,4]))