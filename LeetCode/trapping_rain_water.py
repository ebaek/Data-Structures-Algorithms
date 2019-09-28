# 42: Trapping Rain Water


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        leftMaxHeight, rightMaxHeight, vol = 0, 0, 0

        while left < right:
            leftMaxHeight = max(leftMaxHeight, height[left])
            rightMaxHeight = max(rightMaxHeight, height[right])

            if leftMaxHeight < rightMaxHeight:
                vol += leftMaxHeight - height[left]
                left += 1
            else:
                vol += rightMaxHeight - height[right]
                right -= 1

        return vol
