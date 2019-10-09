# 700: Search in a Binary Search Tree

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val == val: return root
        if not root: return
        
        if root.left and val < root.val:
            return self.searchBST(root.left, val)
        elif root.right:
            return self.searchBST(root.right, val)
        