"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

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