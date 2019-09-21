# 387: First Unique Character in a string

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0: return -1
        if len(s) < 2: return 0

        unique = {}

        for idx, ch in enumerate(s):
            unique.setdefault(ch, []).append(idx)
        
        
        for k,v in unique.items:
            if len(v) == 1: 
                return v[0]

        return -1

# with Counter (squeaky clean)
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = Counter(s)
                
        for idx, ch in enumerate(s):
            if unique[ch] == 1: return idx

        return -1
