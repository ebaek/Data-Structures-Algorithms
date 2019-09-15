# 257: Binary Tree Paths

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None: return []

        allPaths = [str(root.val) + '->' + path for path in (self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right))]

        return [str(root.val)] if len(allPaths) == 0 else allPaths
