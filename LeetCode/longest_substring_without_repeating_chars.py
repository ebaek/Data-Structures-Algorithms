# 3: Longest Substring Without Repeating Characters

# slow solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)

        current = []
        length, startIdx, endIdx = 0, 0, 0

        while endIdx < len(s):
            if s[endIdx] in current:
                startIdx += 1
                endIdx = startIdx
                current = []
            else:
                current.append(s[endIdx])
                endIdx += 1

            length = max(len(current), length)

        return length
    
# faster solution
# time complexity O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, idx - start + 1)

            used[char] = idx

        return max_length

# sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, subMax = 0, 0, 0
        temp_set = set()

        while end < len(s):
            if s[end] in temp_set:
                temp_set.remove(s[start])
                start += 1
            else:
                temp_set.add(s[end])
                end += 1
                subMax = max(subMax, end-start)

        return subMax
    
    
                

        
        
