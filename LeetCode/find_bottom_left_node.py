# 513: Find Bottom Left Tree Value

from collections import deque

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = deque([(root, 0)])
        levels = {}

        while len(q) > 0:
            node, idx = q.popleft()

            if idx not in levels:
                levels[idx] = []

            levels[idx].append((node.val, idx))

            if node.left:
                q.append((node.left, idx + 1))
            if node.right:
                q.append((node.right, idx + 1))

        depth = len(levels) - 1
        return levels[depth][0][0]
