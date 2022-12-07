from typing import List

class Solution:
    # The key to solving this in a greedy manner is to iterate backwards.
    # That way we can always keep track of the current max in the right portion
    # of the array.
    def replaceElements(self, arr: List[int]) -> List[int]:
        big = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = big
            if tmp > big: big = tmp
        return arr

sol = Solution()
print(sol.replaceElements(arr = [17,18,5,4,6,1]))
print(sol.replaceElements(arr = [400]))