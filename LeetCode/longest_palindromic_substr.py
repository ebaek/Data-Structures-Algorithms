# 5: Longest Palindromic Substring

# Manacher's Algorithm 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lengths = []
        
        for idx in range(len(s)):
            leftIdx = idx - 1
            rightIdx = idx + 1
            
            while s[leftIdx] == s[rightIdx]:
                leftIdx -= 1
                rightIdx += 1
            
            leftIdx += 1
            rightIdx -= 1
            
            lengths.append(rightIdx - leftIdx)
        
        return max(lengths)

# Expand from center
# Time Complexity: O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''
        
        for start in range(len(s)):  # i = start, O = n
            for end in range(len(s), start, -1):  # j = end, O = n^2
                if len(m) >= end-start:  # To reduce time
                    break
                elif s[start:end] == s[start:end][::-1]:
                    m = s[start:end]
                    break
        return m
