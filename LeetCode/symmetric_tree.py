from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#breadth first search 
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True

        q = deque([(root, 0)])
        levels = {}
        
        while q:
            node, level = q.popleft()
            if level not in levels: levels[level] = []
            
            levels[level].append(node.val) if node is not None else levels[level].append(None)

            if node:
                q.append((node.left, level + 1)) if node.left is not None else q.append((None, level + 1))
                q.append((node.right, level + 1)) if node.right is not None else q.append((None, level + 1))

        for level in range(len(levels.keys())):
            if not self.isBal(levels[level]): return False
        
        return True

    def isBal(self, l: List[int]):
        if len(l) is 0: return True
        
        midpoint = math.floor(len(l) / 2)
        
        left = midpoint if len(l) % 2 != 0 else midpoint - 1
        right = midpoint
        
        while right < len(l):
            if l[left] != l[right]: return False
            left -= 1
            right += 1
            
        return True

# depth first search
class Solution:
    def isSymmetric(self, root):
        if not root: return True
        return self.dfs(root.left, root.right)


    def dfs(self, l, r):
        if l and r:
            return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
        return l == r
