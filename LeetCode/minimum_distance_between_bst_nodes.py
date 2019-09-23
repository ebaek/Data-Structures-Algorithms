#783: Minimum Distance Between BST Nodes

# Given a Binary Search Tree (BST) with the root node root, return the minimum 
# difference between the values of any two different nodes in the tree.

# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.

# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

#          4
#        /   \
#      2      6
#     / \    
#    1   3  

# DFS: Approach
# Keep traversing through each node and calculate difference between the two values
# Reassign minimum if difference is less 

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:  
        def dfs(node, currMin):
            self.minBST = min(currMin, self.minBST)

            if node:
                if node.left: dfs(node.left, node.val - node.left.val)
                if node.right: dfs(node.right, node.right.val - node.val)

        self.minBST = float('inf')
        dfs(root, self.minBST)
        return self.minBST

# leet inorder solution
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:  

        def dfs(node):
            if node:
                dfs(node.left)
                self.minBST = min(self.minBST, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)
        
        self.prev = float('-inf')
        self.minBST = float('inf')
        dfs(root)
        
        return self.minBST

# [90,69,null,49,89,null,52,null,null,null,null] => Output: 1

#            90
#        /        \
#      69         null
#     / \        /    \
#   49   89    null    52
#  /  \
# null null
