from typing import List

# Sort intervals by the start of the interval.
# Iterate through, if an interval overlaps with the following interval:
# Merge them and pop the following interval.
# O(n) and works in place.
class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        i = 0
        while i <= len(intervals)-2:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i += 1

        return intervals

sol = Solution()
print(sol.merge([[8,10],[15,18],[1,3],[2,6]]))
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[4,5]]))