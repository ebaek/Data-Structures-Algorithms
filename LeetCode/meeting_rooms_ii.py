#253: Meeting Rooms II

# Given an array of meeting time intervals consisting of start 
# and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum 
# number of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1


# Approach: 
# Sort the meetings by their start times because want to compare meetings that 
# have already started 
# Iterate over the sorted meeting times and if in the priority queue the min (end time that ends the earliest)
# is <= meeting's start time, pop off the min
# Add meeting to priority queue 
# Return length of the queue 


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        freeRooms = []
        intervals.sort(key=lambda x: x[0])

        heapq.heappush(freeRooms, intervals[0][1])

        for meeting in intervals[1:]:
            # check if meeting end time is less than potential new meeting's start time
            if freeRooms[0] <= meeting[0]:
                heapq.heappop(freeRooms)
            
            # add meeting's end time to free rooms
            heapq.heappush(freeRooms, meeting[1])
        
        return len(freeRooms)

