# 98: Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 
#    2
#   / \
#  1   3

# Input: [2,1,3]
# Output: true

# Approach: Post Order because checking left child and right child before root
# Check if only left child: max would be root value
# Check if only right child: min would be root value
# If not children check if min < root value < max

# Recursive Approach
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, Min, Max):
            if root is None:
                return True

            if not root.left and not root.right:
                if Min < root.val < Max:
                    return True
                else:
                    return False

            # only right leaf
            if not root.left and root.right:
                return root.val < root.right.val and helper(root.right, root.val, Max)
            # only left leaf
            elif root.left and not root.right:
                return root.val > root.left.val and helper(root.left, Min, root.val)
            # both right and left leaves
            else:
                return root.left.val < root.val < root.right.val and helper(root.left, Min, root.val) and helper(root.right, root.val, Max)

        return helper(root, float('-inf'), float('inf'))


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            root, Min, Max = stack.pop()
            if root:
                if not (Min < root.val < Max):
                    return False
                stack.append((root.left, Min, root.val))
                stack.append((root.right, root.val, Max))

        return True

   






