from typing import List


class Solution:
    # Solution using a dictionary.
    # Since elements can occur multiple times and must have the same rank,
    # this makes it tricky to just sort a list of indices.
    # Instead, it is easier to create a hashmap.
    # Create a sorted version of the array and rank from lowest to highest.
    # Map numbers to rank with dictionary, and finally map the original array
    # to the ranks.
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(arr)
        rankMap = dict()
        rank = 0
        for n in sortedArr:
            if n not in rankMap:
                rank += 1
                rankMap[n] = rank

        return [rankMap[n] for n in arr]

sol = Solution()
print(sol.arrayRankTransform(arr = [40,10,20,30]))
print(sol.arrayRankTransform(arr = [100,100,100]))
print(sol.arrayRankTransform(arr = [37,12,28,9,100,56,80,5,12]))