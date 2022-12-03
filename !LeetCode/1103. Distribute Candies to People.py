from typing import List


class Solution:
    # It is quite efficient to just iterate through and distribute the candies.
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i = 0
        give = 1
        while candies > 0:
            res[i] += give
            candies -= give
            give += 1
            if give > candies: give = candies
            i += 1
            if i == num_people: i = 0
        return res

sol = Solution()
print(sol.distributeCandies(candies = 7, num_people = 4))
print(sol.distributeCandies(candies = 10, num_people = 3))