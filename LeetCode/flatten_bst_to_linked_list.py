# 114: Flatten Binary Tree to Linked List

# Approach: use a stack to save the left and right values

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root: return None
        stack = [root]
        
        prev = None
        
        while stack:
            node = stack.pop()
            
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            
            node.left, node.right = None, None
            
            if prev: prev.right = node
            prev = node
            
        return root