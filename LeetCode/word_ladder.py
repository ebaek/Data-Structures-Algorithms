# 127: Word Ladder


from collections import defaultdict, deque 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pathLength = float('infinity')
        wordList.append(beginWord)
        graph = self.buildGraph(wordList)
        visited = set()
        
        q = deque([(beginWord, 0)])
        
        while q:
            word, path = q.popleft()
            visited.add(word)
            
            if word == endWord: 
                pathLength = min(pathLength, path)
                continue
            
            for chIdx in range(len(word)):
                for neighbor in graph[word[:chIdx] + "*" + word[chIdx+1:]]:
                    if neighbor not in visited: 
                        q.append((neighbor, path+1))
        
        if pathLength == float('infinity'): return 0
        return pathLength+1
        
    def buildGraph(self, wordList):
        wordLength = len(wordList[0])
        graph = defaultdict(list)
        
        for word in wordList:
            for chIdx in range(wordLength):
                graph[word[:chIdx] + "*" + word[chIdx+1:]].append(word)
        
        return graph