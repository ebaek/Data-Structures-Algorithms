#14: Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if len(strs) < 2: return strs[0]
        longest, idx = "", 0
        
        while True:
            if idx >= len(strs[0]): break
            ch = strs[0][idx]
            
            for word in strs:
                if idx >= len(word) or word[idx] != ch: return longest
            
            longest += ch
            idx += 1
        
        return longest 