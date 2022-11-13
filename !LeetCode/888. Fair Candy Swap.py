from typing import List


class Solution:
    # Solution using hashset to solve in linear time.
    # Find the amount of candy that each person must have at the end.
    # This is the average amount, which we know is an integer since a valid output is guaranteed.
    # Turn Bob's box sizes into a hashset.
    # Go through all Alice's boxes and calculate how big a box Bob must give back for alize to reach target.
    # If Bob has a box of that size, return those sizes.
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum, bobSum = sum(aliceSizes), sum(bobSizes)
        target = abs(aliceSum + bobSum) // 2 # Since there is a guaranteed valid output, we know the sum of all candy is divisible by two
        bobset = set(bobSizes)
        for aliceGives in aliceSizes:
            bobMustReturn = target - (aliceSum - aliceGives)
            if bobMustReturn in bobset: return [aliceGives, bobMustReturn]

sol = Solution()
print(sol.fairCandySwap(aliceSizes = [1,1], bobSizes = [2,2]))
print(sol.fairCandySwap(aliceSizes = [1,2], bobSizes = [2,3]))
print(sol.fairCandySwap(aliceSizes = [2], bobSizes = [1,3]))