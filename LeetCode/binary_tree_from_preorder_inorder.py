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
    

class Solution(object):
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_dict = {}
        
        for idx, num in enumerate(inorder):
            inorder_dict[num] = idx
            
        pre_iter = iter(preorder)

        def helper(start, end):
            if start > end: return None
            
            root_val = next(pre_iter)
            root = TreeNode(root_val)
            
            idx = inorder_dict[root_val]
            
            root.left = helper(start, idx-1)
            root.right = helper(idx+1, end)
            return root

        return helper(0, len(inorder) - 1)

                
