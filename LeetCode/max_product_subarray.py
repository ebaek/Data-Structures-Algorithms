# 152: Maximum Product Subarray

# Approach:
# keep track of local min and local max while iterating to numbers
# if the element is < 0, need to compare localMax to localMin*currentElement
# otherwise if element is >= 0 need to compare localMAx to localMax*currentElement

# Time Complexity: O(N)
# Space Complexity: O(2N)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return
        localMin, localMax = [0] * len(nums), [0] * len(nums)

        localMin[0] = localMax[0] = globalMax = nums[0]

        for idx in range(1, len(nums)):
            if nums[idx] < 0:
                localMax[idx] = max(localMin[idx-1]*nums[idx], nums[idx])
                localMin[idx] = min(localMax[idx-1]*nums[idx], nums[idx])
            else:
                localMax[idx] = max(localMax[idx-1]*nums[idx], nums[idx])
                localMin[idx] = min(localMin[idx-1]*nums[idx], nums[idx])

            globalMax = max(localMax[idx], globalMax)

        return globalMax
