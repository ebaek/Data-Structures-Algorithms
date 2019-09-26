# 230: Kth Smallest Element in a BST

# Given a binary search tree, write a function kthSmallest to find 
# the kth smallest element in it.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
#   3
#  / \
# 1   4
#  \
#   2
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1

# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to 
# find the kth smallest frequently? How would you optimize the kthSmallest routine?

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Approach: use a queue and append all node.left 
# in a second iteration, keep poplefting until reach count. if the popped node has a node.right
# count += 1, else node += 1

# Time Complexity: O(log(n) + k)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1

            if not k: return root.val

            root = root.right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def inorder(root):
            if root:
                return inorder(root.left) + [root.val] + inorder(root.right)
            else:
                return []

        return inorder(root)[k-1]

                
            
            
        
                

        
        
        
