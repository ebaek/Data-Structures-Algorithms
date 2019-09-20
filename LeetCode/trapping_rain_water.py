# 42: Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lMax, rMax, vol = 0, 0, 0

        while left < right:
            lMax = max(lMax, height[left])
            rMax = max(rMax, height[right])

            if lMax >= rMax:
                vol += rMax - height[right]
                right -= 1
            else:
                vol += lMax - height[left]
                left += 1
            
        return vol 
