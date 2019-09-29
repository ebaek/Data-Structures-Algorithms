# 347: Top K Frequent Elements 

# Solution
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. 
# If two words have the same frequency, then the word with the lower alphabetical order comes first.

from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFreq = Counter(words)
        wordFreq = sorted(wordFreq.items(),
                          key=lambda pair: pair[1], reverse=True)
        count = 0
        mostFreq = []

        for key, val in wordFreq:
            if count == k: break
            mostFreq.append(key)
            count += 1

        return mostFreq
    


