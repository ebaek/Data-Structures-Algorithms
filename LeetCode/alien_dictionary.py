# 269: Alien Dictionary

from typing import List
from collections import defaultdict

# Approach: topological sort in order to check that all characters can be visited 
# in a non-cyclical way

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # calculate all edges (u->v, in which u must be ahead of v in alien dictionary)
        edges = defaultdict(set)
        degrees = defaultdict(int)
        for two_words in zip(words, words[1:]): # compare adjacent words
            for ch1, ch2 in zip(*two_words): # compare letter by letter between two words
                if ch1 != ch2: # ch1 -> ch2 (degree[ch2]++)
                    edges[ch1].add(ch2) # ch2 depends on (is after) ch1
                    break 

        # calculate in-degrees for all vertices
        for ch in edges.keys():
            for ch2 in edges[ch]:
                degrees[ch2] += 1
        
        charset = set(''.join(words)) # get all vertices
        eligible_nodes = [ch for ch in charset if ch not in degrees] # degree=0 as start nodes
        alien_list = []
        while eligible_nodes:
            ch = eligible_nodes.pop(0)
            alien_list.append(ch)
            for ch2 in edges[ch]:
                degrees[ch2] -= 1
                if degrees[ch2] == 0:
                    eligible_nodes.append(ch2)
                    
        if len(alien_list) == len(edges.keys()):  # all vertex in degrees are zero, acyclic graphs
            return ''.join(alien_list)
        return '' # otherwise, circle found in graph
