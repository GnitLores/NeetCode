import collections
from typing import List


class Solution:
    # Iterate through list 1, count the occurrences of elements that
    # appear in list 2, and note elements that don't appear in list 2.
    # Construct output by using count in the order that elements appear in list 2
    # and then append the sorted list of numbers that don't appear.
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = collections.defaultdict(int)
        notInList = []
        hashset = set(arr2)

        for n in arr1:
            if n in hashset:
                count[n] += 1
            else:
                notInList.append(n)
        
        res = []
        for n in arr2:
            res += [n] * count[n]
        res += sorted(notInList)
        return res

sol = Solution()
print(sol.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
print(sol.relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]))