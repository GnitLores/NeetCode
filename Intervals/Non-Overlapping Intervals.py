from typing import List

# If we have overlapping intervals:
# When iterating from beginning, the optimal choice is to remove interval that ends latest.
# It has greatest potential to overlap with other intervals.
# Sort intervals by start.
# Iterate through adding intervals to a list.
# If there is overlap, add interval with earliest end.
# O(nlogn) because of sort.
class Solution(object):
    def eraseOverlapIntervals(self, intervals: List[List]):
        intervals.sort()
        res =  []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < res[-1][1]:
                if intervals[i][1] < res[-1][1]:
                    res[-1] = intervals[i]
            else:
                res.append(intervals[i])

        return len(intervals) - len(res)
    
sol = Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(sol.eraseOverlapIntervals([[1,2],[2,3]]))