# 515: Find Largest Value in Each Tree Row

# Example:
# Input:

#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 

# Output: [1, 3, 9]
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root == None: return []

        q = deque([(root, 0)])
        levels = {}

        while q:
            ele, level = q.popleft()
            if level not in levels: levels[level] = []
            levels[level].append(ele.val)

            if ele.left is not None: q.append((ele.left, level + 1))
            if ele.right is not None: q.append((ele.right, level + 1))

        return [max(levels[level]) for level in levels.keys()]
            
            
        
        
