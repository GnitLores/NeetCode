from tkinter import N
from typing import List
import math


class Solution:
    # FIrst find the integer value the count of a number must reach to exceed 25 percent.
    # This must be the integer division by 4 plust 1 (since integer division rounds down).
    # Iterate throguh the array, checking when we encounter a new number and count the
    # occurrences.
    # The moment the limit is reached, abandon the search and return that number.
    def findSpecialInteger(self, arr: List[int]) -> int:
        limit = (len(arr) // 4) + 1
        cnt = 0
        number = None
        for n in arr:
            if n == number:
                cnt += 1
            else:
                cnt = 1
                number = n
            if cnt == limit:
                return n

sol = Solution()
print(sol.findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))
print(sol.findSpecialInteger(arr = [1,1]))