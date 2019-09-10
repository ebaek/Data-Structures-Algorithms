# 47 Permutations II

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answers, flags = [], [False]*len(nums)
        nums.sort()
        self.dfs(nums, flags, [], answers)
        return answers

    def dfs(self, nums, flags, set, answers):
        if len(nums) == len(set):
            answers.append(set)
            return
        for i in range(len(nums)):
            if not flags[i]:
                if i > 0 and not flags[i-1] and nums[i] == nums[i-1]:
                    continue
                flags[i] = True
                self.dfs(nums, flags, set+[nums[i]], answers)
                flags[i] = False
