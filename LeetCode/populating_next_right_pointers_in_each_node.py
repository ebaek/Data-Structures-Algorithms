# 116: Populating Next Right Pointers in Each Node

# Populate each next pointer to point to its next right node. 
# If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.
"""
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import dequeue 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q = deque([(root, 0)])
        dict = {}

        while q:
            node, level = q.popleft()
            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))

            if level not in dict: 
                dict[level] = node
                node.next = None
            else:
                lastNode = dict[level]
                lastNode.next = node
                node.next = None
                dict[level] = node

        return root





