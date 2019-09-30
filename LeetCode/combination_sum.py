# 39: Combination Sum

# Given a set of candidate numbers (candidates) (without duplicates) 
# and a target number (target), find all unique combinations in 
# candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

# Approach: 
# base case: there are no more potential candidates
# recursive case iterate through all potential candidates
# recursive step -> shorten the candidates list with numbers less than the target


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []

        def helper(combo, idx, newTarget):
            if newTarget == 0:
                combos.append(combo)
            else:
                for i in range(idx, len(candidates)):
                    if newTarget - candidates[i] >= 0:
                        helper(combo + [candidates[i]], i, newTarget-candidates[i])


        return combos

            
class Solution:
    def combinationSum(self, candidates, target):
        combos = []
        candidates.sort()

        def dfs(target, index, path):
            if target < 0: return 
            if target == 0:
                combos.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(target-candidates[i], i, path+[candidates[i]])

        dfs(target, 0, [])
        return combos
