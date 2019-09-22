# 687. Longest Univalue Path

# Given a binary tree, find the length of the longest path where each node in the path has the same value. 
# This path may or may not pass through the root.

# The length of path between two nodes is represented by the number of edges between them.

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS Approach: 
    # continue to explore path as long as the node is the same as the previous node, keep track of count
    # if the node's value isn't the same, return  


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longestPath = 0

        def dfs(node):
            if not node:
                return 0

            leftPath, rightPath = dfs(node.left), dfs(node.right)
            leftPathLength = rightPathLength = 0

            if node.left and node.left.val == node.val:
                leftPathLength = 1 + leftPath
            if node.right and node.right.val == node.val:
                rightPathLength = 1 + rightPath

            self.longestPath = max(self.longestPath, leftPathLength + rightPathLength)
            return max(leftPathLength, rightPathLength)

        dfs(root)
        return self.longestPath

 
