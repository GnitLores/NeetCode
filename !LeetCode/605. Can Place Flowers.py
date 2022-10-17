from typing import List


class Solution:
    # The main issue is boundary conditions.
    # - n being 0
    # - Flowebed being very small.
    # - Edge elements only have one neighbor.
    #
    # Once we have checked all these boundary conditions,
    # we can just iterate through the array exluding the edge elements
    # and check for groups of three consecutive zeros.
    # If the flowerbed is two elements long, there are no elements to
    # iterate through as they are both edge elements.
    # Consequently, the boundary condition checks deal with the two element
    # case without any need to enter the loop.
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        if len(flowerbed) == 1: return flowerbed[0] == 0 and n <= 1

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-2] == 0 and flowerbed[-1] == 0:
            flowerbed[-1] = 1
            n -= 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0
        


sol = Solution()
print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
print(sol.canPlaceFlowers(flowerbed = [0,0,0,0,0], n = 2))