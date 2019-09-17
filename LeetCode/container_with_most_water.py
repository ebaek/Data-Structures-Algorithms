# 11: Container with Most Water 

#brute force 
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0
        totalHeights = len(heights)
        
        for start in range(totalHeights):
            for end in range(start, totalHeights):
                height = min(heights[start], heights[end])
                
                currentVol = height * (end - start)
                
                if currentVol >= vol: vol = currentVol
        
        return currentVol
    

# time complexity: O(n)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end, vol = 0, len(heights) - 1, 0

        while start <= end:
            width = end - start
            startHeight, endHeight = heights[start], heights[end]
            height = min(startHeight, endHeight)

            if width * height >= vol:
                vol = width * height

            if startHeight >= endHeight:
                end -= 1
            else:
                start += 1

        return vol
        
