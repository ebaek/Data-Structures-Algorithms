# 692: Top K Frequent Words

from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        candidates = sorted(count.keys(), key = lambda word: (-count[word], word))
        return candidates[:k]