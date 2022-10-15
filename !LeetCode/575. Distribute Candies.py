from typing import List


class Solution:
    # If the number of candies that can be eaten is smaller than the
    # number of unique candy types, this is the number of types that can
    # be eaten, as they will eat only different types.
    # Otherwise, it is the number of unique candy types, as that is the
    # max number of types that can be eaten regardless of how much candy they
    # can eat.
    # Find unique types by converting to set, and find the minimum of the two values.
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))

sol = Solution()
print(sol.distributeCandies(candyType = [1,1,2,2,3,3]))
print(sol.distributeCandies(candyType = [1,1,2,3]))
print(sol.distributeCandies(candyType = [6,6,6,6]))