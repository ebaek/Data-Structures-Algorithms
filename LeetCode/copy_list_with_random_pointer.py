"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

from collections import deque
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        
        current = head 
        copy = Node(head.val, head.next, head.random)
        
        firstIteration = copy
        secondIteration = copy
        
        store = {}
                
        while head:
            store[firstIteration.val] = firstIteration
            if head.next: firstIteration.next = Node(head.next.val, None, None) 
            firstIteration = firstIteration.next
            head = head.next
        
        while current:
            if current.random:
                secondIteration.random = store[current.random.val]
                
            if current.next:
                secondIteration.next = store[current.next.val]
            
            current = current.next
            secondIteration = secondIteration.next
        
        return copy 

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        pointer = Node(head.val, None, None)
        dupedNodes = {pointer.val: pointer}
        q = deque([head])

        dupedNode = None

        def helper(tmpNode):
            if tmpNode.val not in dupedNodes:
                dupedNodes[tmpNode.val] = Node(tmpNode.val, None, None)
            return dupedNodes[tmpNode.val]

        while q:
            tmpNode = q.popleft()

            dupedNode = helper(tmpNode)

            if tmpNode.next:
                dupedNode.next = helper(tmpNode.next)
                q.append(tmpNode.next)

            if tmpNode.random:
                dupedNode.random = helper(tmpNode.random)

        return pointer
