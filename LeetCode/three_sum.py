# 15: 3 Sum

# brute force solution
# O(n^2)
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        if len(nums) < 2:
            return []

        threeSums = []
        start, mid, end = 0, 1, 2

        while start < end and end < len(nums):
            startNum, midNum, endNum = nums[start], nums[mid], nums[end]

            if startNum + midNum + endNum == 0:
                currentThree = [startNum, midNum, endNum]
                if currentThree not in threeSums:
                    threeSums.append(currentThree)

            if end is not len(nums) - 1:
                if mid == end:
                    start += 1
                    mid = start + 1
                    end = mid + 1
                else:
                    end += 1
            else:
                if mid == len(nums) - 2:
                    start += 1
                    mid = start + 1
                    end = mid + 1
                else:
                    mid += 1
                    end = mid + 1

        return threeSums
    
a = [10,-2,-12,3,-15,-12,2,-11,3,-12,9,12,0,-5,-4,-2,-7,-15,7,4,-5,-14,-15,-15,-4,10,9,-6,7,1,12,-6,14,-15,12,14,10,0,10,-10,3,4,-12,10,7,-9,-7,-15,-8,-15,-4,2,9,-4,3,-10,13,-3,-1,5,5,-4,-15,4,-11,4,-4,6,-11,-9,12,7,11,7,2,-5,13,10,-5,-10,3,7,0,-3,10,-12,2,9,-8,8,-9,13,12,13,-6,8,3,5,-9,7,12,10,-8,0,2,1,10,-7,-3,-10,-10,7,4,5,-11,-8,0,-2,-14,8,13,-8,-2,10,13]
sol = Solution()
print(sol.threeSum(a))

class Solution(object):
	def threeSum(self, nums):
		res = []
		nums.sort()
		length = len(nums)

		for i in range(length-2): 
			if nums[i] > 0: break  
			if i > 0 and nums[i] == nums[i-1]: continue

			l, r = i+1, length-1
   
			while l < r:
				total = nums[i]+nums[l]+nums[r]

				if total < 0: l += 1
				elif total > 0: r -= 1
				else: 
					res.append([nums[i], nums[l], nums[r]])
					while l < r and nums[l] == nums[l+1]:
						l += 1
					while l < r and nums[r] == nums[r-1]:
						r -= 1
					l += 1
					r -= 1
		return res
