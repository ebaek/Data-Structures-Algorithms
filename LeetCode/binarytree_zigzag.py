# 103: Binary Tree Zigzag Level Order Traversal

from collections import deque, defaultdict

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        nodeDict = defaultdict(list)
        zigZag = []
        q = deque([(root, 0)])
        
        while q:
            node, level = q.popleft()
            
            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))

            nodeDict[level].append(node.val)
        
        for level, nodeList in nodeDict.items():
            if level % 2 == 0:
                zigZag.append(nodeList)
            else:
                zigZag.append(nodeList[::-1])
        
        return zigZag
