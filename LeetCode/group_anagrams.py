
# 49: Group Anagrams

# Time Complexity: O(a*nlogn)
# Space Complexity: O(n)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWords = defaultdict(list)
        
        for word in strs:
            sortedWord = "".join(sorted(word))
            sortedWords[sortedWord].append(word)
        
        grouped = [val for key, val in sortedWords.items()]
        
        return grouped