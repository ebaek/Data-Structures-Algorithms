
# 72: Edit Distance

# Approach:
# Dynamic Programming: tabulation

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1Length, word2Length = len(word1), len(word2)
        table = [ [0]*(word2Length+1) for _ in range(word1Length+1)]
        
        for idx in range(word1Length+1):
            table[idx][0] = idx
        
        for idx in range(word2Length+1):
            table[0][idx] = idx
        
        for word1Idx in range(1, word1Length+1):
            for word2Idx in range(1, word2Length+1):
                if word1[word1Idx-1] == word2[word2Idx-1]:
                    table[word1Idx][word2Idx] = table[word1Idx-1][word2Idx-1]
                else:
                    insert = table[word1Idx-1][word2Idx]
                    replace = table[word1Idx-1][word2Idx-1]
                    delete = table[word1Idx][word2Idx-1]
                    table[word1Idx][word2Idx] = min(insert, replace, delete) + 1
        
        return table[-1][-1]
