from typing import List


class Solution:
    # Add up each interval, taking the min of the full interval and the interval to
    # the next event.
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        for i, t in enumerate(timeSeries):
            if i < len(timeSeries) - 1:
                res += min(duration, timeSeries[i + 1] - t)
            else:
                res += duration
        return res

sol = Solution()
print(sol.findPoisonedDuration(timeSeries = [1,4], duration = 2))
print(sol.findPoisonedDuration(timeSeries = [1,2], duration = 2))