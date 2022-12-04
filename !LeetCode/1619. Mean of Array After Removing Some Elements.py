from typing import List


class Solution:
    # This can technically be done in O(n) time, but it seems efficient and much simpler
    # to sort and calculate the average of the trimmed section.
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        trim = n // 20
        return sum(arr[trim : (n - trim)]) / (n - 2 * trim)
sol = Solution()
print(sol.trimMean(arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]))
print(sol.trimMean(arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]))
print(sol.trimMean(arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))