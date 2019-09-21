# 94: Binary Tree Inorder Traversal

# recursive solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:        
        def traverse(root, nodes):
            if root: 
                traverse(root.left, nodes)
                path.append(root.val)
                traverse(root.right, nodes)
        
        path = []
        traverse(root, path)

        return path 

from collections import deque 

# iterative solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        path = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                path.append(tmpNode.val)
                root = tmpNode.right

        return path