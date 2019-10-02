# 139: Word Break

# Recursive Approach:

# BASE CASE
# if s is an empty string, return True 

# RECURSIVE STEP
# convert wordDict into set for O(1) look up time
# check if word exists in the set starts at 0 -> idx, if exists than recursively call wordBreak
# with a string from s[idx:] 
#   -> if this returns True, return True
#   -> if can't find a word in the list, return False 


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        
        def search(s):
            if s in wordDict: return True 
            
            for idx in range(len(s)+1):
                if s[:idx] in wordSet:
                    if search(s[idx:]): return True
                    
            return False
        
        return search(s)
    

# With memoization
# Memoization: Time Complexity -> O(N ^2)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def search(s):
            if s in memo:
                return memo[s]
            if s in wordDict:
                return True

            for idx in range(len(s)+1):
                if s[:idx] in wordSet:
                    if search(s[idx:]):
                        memo[s] = True
                        return True

            memo[s] = False
            return memo[s]

        return search(s)
