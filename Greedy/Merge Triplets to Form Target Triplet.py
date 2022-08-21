from typing import List


class Solution:
    # Because we can only use max operation on an entire triplet,
    # if any triplet value is greater than the targert, that triplet cannot be used.
    # For triplets that obey this, if there is a value equal to the target value,
    # the target value can be obtained.
    # If all three values can be obtained, obtaining the triplet is possible.
    # O(n) time.
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        isPossible = [False] * 3

        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue

            if trip[0] == target[0]: isPossible[0] = True
            if trip[1] == target[1]: isPossible[1] = True
            if trip[2] == target[2]: isPossible[2] = True

        return all(isPossible)

sol = Solution()
print(sol.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))
print(sol.mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))