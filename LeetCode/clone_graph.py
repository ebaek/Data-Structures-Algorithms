# 133: Clone Graph

# Approach: breadth first search, maintain a visited, maintain a dictionary
# that stores reference to copy of node along with copy of a node as value 

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

from collections import deque, defaultdict

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        copyDict = defaultdict(None)
        visited = set()
        q = deque([node])
        
        while q:
            currNode = q.popleft()
            
            if currNode.val not in copyDict: copyDict[currNode.val] = Node(currNode.val, [])
            if currNode.val not in visited:
                for neighbor in currNode.neighbors:
                    if neighbor.val not in copyDict: copyDict[neighbor.val] = Node(neighbor.val, [])

                    if neighbor not in visited:
                        copyDict[currNode.val].neighbors.append(copyDict[neighbor.val])

                    q.append(neighbor)
            
            visited.add(currNode.val)          
        
        return copyDict[node.val]
