# 56: Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# Note: input types have been changed on April 15, 2019. 
# Please reset to default code definition to get new method signature.

# Approach: Sort by value of start time, then iterate through elements
# to check if the start time of new element is less than end. if so, swap.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        merged = [] 
        
        for interval in intervals:
            if not merged: 
                merged.append(interval)
                continue
        
            lastStart, lastEnd = merged[-1]    
            currStart, currEnd = interval

            if currStart > lastEnd:
                merged.append([currStart, currEnd])
            else:
                end = max(lastEnd, currEnd)
                merged[-1] = [lastStart, end]
        
        return merged
