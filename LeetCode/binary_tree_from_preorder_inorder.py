# 105: Construct Binary Tree from Preorder and Inorder Traversal

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0: return 
        root = TreeNode(preorder[0])
        
        leftInorder = inorder[0:inorder.index(root.val)]
        rightInorder = inorder[inorder.index(root.val)+1:]
        
        leftPreorder = []
        rightPreorder = []
        
        for el in preorder:
            if el in leftInorder: leftPreorder.append(el)
            if el in rightInorder: rightPreorder.append(el)
        
        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)
        
        return root 