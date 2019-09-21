# 242: Valid Anagram


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anDict = {}
        doneCount = 0

        for idx in range(len(s)):
            if s[idx] not in anDict: anDict[s[idx]] = 0
            anDict[s[idx]] += 1
        
        for idx in range(len(t)):
            if t[idx] in anDict:
                anDict[t[idx]] -= 1 
            else:
                return False

        for key, val in anDict.items():
            if val != 0: return False
        
        return True
    
# using counter 

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount, tCount = Counter(s), Counter(t)

        for key, val in sCount.items():
            if val != tCount[key]: return False

        return True

