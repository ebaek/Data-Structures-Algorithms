# 199. Binary Tree Right Side View



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Given a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Approach: BFS and for each level replace the value if value exists with value of node,
# otherwise, create a key with the value pointing to the nodes value
# iterate through the values of the dictionary and append the values to a list

from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        q = deque([(root, 0)])
        dict = {}

        while q:
            node, level = q.popleft()
            
            dict[level] = node.val
            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))
        
        rightSides = []

        for nodeVal in dict.values():
            rightSides.append(nodeVal)
        
        return rightSides
        
        