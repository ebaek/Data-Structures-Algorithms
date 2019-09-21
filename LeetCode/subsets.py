# 78: Subsets 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, idx, path, res):
            res.append(path)

            for i in range(len(nums)):
                dfs(nums, i+1, path + [nums[i]], res)
        
        res = []
        dfs(nums, 0, [], res)
        return res 