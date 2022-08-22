# Given an array of meeting time intervals consisting of start and
# end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number
# of conference rooms required.)

from typing import List
import heapq

class Solution:
    # Solution using minheap.
    # Sort the intervals by start time.
    # Make a minheap where with an element for each room, where the value is
    # the end time of the meeting currently assigned to that room.
    # For each interval, peek at the earliest end time in the heap.
    # If it can accomodate the interval, pop it and push the new end time.
    # If the earliest end time doesn't accomodate the interval, push the end time
    # which creates a new room.
    # O(nlogn) because we sort and because heappush and heappop are O(logn).
    def minMeetingRooms(self, intervals: List) -> int:
        intervals.sort()
        rooms = [0] # Only one room with no meeting at first
        for inter in intervals:
            if inter[0] >= rooms[0]: # If room with earliest end time is valid
                heapq.heappop(rooms)
                heapq.heappush(rooms, inter[1]) # Reinsert with new end time
            else:
                heapq.heappush(rooms, inter[1]) # Create new rooom

        return len(rooms)


    # Solution without heap.
    # Sort all the start times and end times.
    # Iterate through them all and check if the next time is start or end time.
    # If start time - start a concurrent meeting.
    # If end time - end a meeting.
    # Meetings starting and ending at the same time do not overlap, so end before starting.
    # We need as many rooms as there are max concurrent meetings.
    # Doesn't need a heap, but sorts twice and code is a bit more complicated.
    # Also O(nlogn).
    def minMeetingRoomsTimes(self, intervals: List) -> int:
        starts = sorted([x[0] for x in intervals])
        ends = sorted([x[1] for x in intervals])

        maxRooms = concurrent = iStart = iEnd = 0
        while iStart < len(starts) and iEnd < len(ends):
            if iEnd >= len(ends) or starts[iStart] < ends[iEnd]: # < and not <= because end take priority
                concurrent += 1
                iStart += 1
            else:
                concurrent -= 1
                iEnd += 1
            maxRooms = max(maxRooms, concurrent)

        return maxRooms

sol = Solution()
print(sol.minMeetingRooms([(0,30),(5,10),(15,20)]))
print(sol.minMeetingRooms([(2,7)]))
print(sol.minMeetingRooms([(0,30),(5,10),(15,20),(45,50),(50,55),(55,60),(47,57),(49,53)]))
print("")
print(sol.minMeetingRoomsTimes([(0,30),(5,10),(15,20)]))
print(sol.minMeetingRoomsTimes([(2,7)]))
print(sol.minMeetingRoomsTimes([(0,30),(5,10),(15,20),(45,50),(50,55),(55,60),(47,57),(49,53)]))