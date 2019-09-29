# 430. Flatten a Multilevel Doubly Linked List

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        current = head
        
        while current:
            if not current.child:
                current = current.next
            else:
                subCurrent = current.child
                
                while subCurrent.next:
                    subCurrent = subCurrent.next
                    
                subCurrent.next = current.next
                
                if current.next:
                    current.next.prev = subCurrent
                    
                current.next = current.child
                current.child.prev = current
                current.child = None
        return head
    
# Using a stack approach
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = []
        subPointer = head

        while subPointer:
            if subPointer.child:
                if subPointer.next: stack.append(subPointer.next)
                subPointer.next = subPointer.child
                subPointer.child.prev = subPointer
                subPointer.child = None

            elif not subPointer.next and stack:
                subPointer.next = stack.pop()
                subPointer.next.prev = subPointer

            subPointer = subPointer.next

        return head



