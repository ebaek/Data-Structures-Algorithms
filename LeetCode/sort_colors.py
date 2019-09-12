# 75: Sort Colors 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        idx, low, high = 0, 0, len(nums) - 1

        while idx <= high:
            if nums[idx] == 2:
                nums[idx], nums[high] = nums[high], nums[idx]
                high -= 1
            elif nums[idx] == 0:
                nums[idx], nums[low] = nums[low], nums[idx]
                low += 1
                idx += 1
            else:
                idx += 1
