# 104: Maximum Depth of Binary Tree


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        self.max_count = 1

        def dfs(count, node):
            if not node.left and not node.right:
                self.max_count = max(self.max_count, count)
            if node.left:
                dfs(count+1, node.left)
            if node.right:
                dfs(count+1, node.right)

        dfs(self.max_count, root)
        return self.max_count
