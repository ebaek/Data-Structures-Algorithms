# 938: Range Sum of BST

# Given the root node of a binary search tree, return the sum of values of all nodes 
# with value between L and R (inclusive).

# The binary search tree is guaranteed to have unique values.

# Example:
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

#       10 
#    5      15        => 32 because node values include [7,5,10,15] => [7,10,15]
#  3  7  null 18 

# Approach:

# DFS because want to traverse tree children of nodes and extract their values 
    # keep exploring paths until reach either left or right node, if current node is 
    # within bounds of l and r add node's value to the sum

    # base case: if not a node don't do anything
    
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.currSum = 0

        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.currSum += node.val
                if node.val < R: dfs(node.right)
                if node.val > L: dfs(node.left)
        
        dfs(root)
        return self.currSum 





