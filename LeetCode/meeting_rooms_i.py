# 252: Meeting Rooms I
# Given an array of meeting time intervals consisting of start and end 
# times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could 
# attend all meetings.

# Example 1:

# Input: [[0,30],[5,10],[15,20]]
# Output: false

# Example 2:
# Input: [[7,10],[2,4]]
# Output: true


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        for idx, interval in enumerate(intervals):
            currentStart, currentEnd = interval

            lastEnd = None
            if idx > 0: lastStart, lastEnd = intervals[idx-1]

            if lastEnd and currentStart < lastEnd: return False

        return True
