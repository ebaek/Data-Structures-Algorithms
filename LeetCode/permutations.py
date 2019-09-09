class Solution:
    def permute(self, nums):
        answers = []
        self.dfs(nums, [], answers)
        return answers

    def dfs(self, nums, set, answers):
        if not nums:
            answers.append(set)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], set+[nums[i]], answers)
