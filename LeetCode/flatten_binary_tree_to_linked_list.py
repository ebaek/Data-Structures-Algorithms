# 114: Flatten Binary Tree to Linked List
# Given a binary tree, flatten it to a linked list in-place.

# For example, given the following tree:

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# Approach: 
# if node.left and node.right:
    # flatten left
    # flatten right
    # last element on left.right = root.right
    # root.right = root.left
    # root.left = null

# if node.left and not node.right:
    # flatten left
    # node.right = left
    # left = null

# if node.right and not node.left:
    # flatten right
    # return

# if node is null:
    # return 

class Solution:
    def flatten(self, root: TreeNode) -> None:
        def flattenHelper(root):
            if root is None: return

            left = flattenHelper(root.left)
            right = flattenHelper(root.right)

            if right is None and left is None:
                return root
            elif left is None:
                return right
            elif right is None:
                root.right = root.left
                root.left = None
                return left
            else:
                tmp = root.right
                root.right = root.left
                root.left = None
                left.right = tmp
                return right
        
        flattenHelper(root)


        




