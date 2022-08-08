class Solution:
    # Sort all intervals by start time and iterate through.
    # For all meetings to be attendable, each meeting must end no later than the beginning of the next meeting.
    # O(nlogn) time because the intervals must be sorted.
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda x: x.start)
        
        endTime = 0
        for n in intervals:
            if n.start < endTime:
                return False
            else:
                endTime = n.end
        return True

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def testSolution(*args):
    obj = Solution()
    res = obj.canAttendMeetings(*args)
    print(res)

testSolution([Interval(0, 30), Interval(5, 10), Interval(15, 20)])
testSolution([Interval(15, 20), Interval(0, 5), Interval(5, 10)])