class Solution(object):
    # Insert interval into list and iterate through, merging intervals.
    # O(n) time. Works in place.
    def insert(self, intervals, newInterval):
        if not intervals:
            intervals.append(newInterval)
            return intervals
        
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                break

        if newInterval[0] > intervals[-1][0]:
            intervals.append(newInterval)
        
        i = 0
        while i <= len(intervals)-2:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i += 1

        return intervals
    
    # Slightly simpler and more efficient solution.
    # Create empy lest and iterate through intervals inserting them into new list.
    # Insert new interval if safe, otherwise merge interval into new interval and try with next.
    # Still O(n) time and uses O(n) extra space.
    def insertSimple(self, intervals, newInterval):
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res


sol = Solution()
print(sol.insert([[1,3],[6,9]], [2,5]))
print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(sol.insertSimple([[1,3],[6,9]], [2,5]))
print(sol.insertSimple([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))