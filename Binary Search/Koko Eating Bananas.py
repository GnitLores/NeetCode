from typing import List
import math

class Solution:
    # Binary search solution.
    # The slowest possible speed is 1 per hour.
    # The fastest possible speed is the size of the greatest pile.
    # Do a binary search while recording slowest succeful attempt.
    # O(log(maxpile)*piles) time complexity.
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)
        slowestSucces = maxSpeed
        while minSpeed <= maxSpeed:
            speed = (minSpeed+maxSpeed) // 2
            totalTime = 0

            for p in piles:
                totalTime += math.ceil(p / speed)

            if totalTime <= h:
                slowestSucces = min(slowestSucces, speed)
                maxSpeed = speed - 1
            else:
                minSpeed = speed + 1

        return slowestSucces

def testSolution(*args):
    sol = Solution()
    res = sol.minEatingSpeed(*args)
    print(res)

testSolution([3,6,7,11],8)
testSolution([30,11,23,4,20],5)
testSolution([30,11,23,4,20],6)