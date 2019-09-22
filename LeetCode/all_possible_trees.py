# 894: All Possible Full Binary Trees

# A full binary tree is a binary tree where each node has exactly 0 or 2 children.

# Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

# Each node of each tree in the answer must have node.val = 0.

# You may return the final list of trees in any order.

# Given a number N -> All Possible Combinations of a Full Binary Tree
# Node has 0 or 2 children

# Hypothesis: Time Complexity is O(2^n) because every node can at worst case have 2 children -> To Confirm!
# Recursive Approach because we are building on previous combination 

# class TreeNode:
    # self.val = x
    # self.left = None
    # self.right = None


class Solution:
    def allPossibleFBT(self, N: int, memo={1: [TreeNode(0)]}) -> List[TreeNode]:
        if N in memo: return memo[N]
        ans = []
                                                          
        for idx in range(N):
            for left in self.allPossibleFBT(idx):
                for right in self.allPossibleFBT(N - idx - 1):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ans += [root]
        memo[N] = ans

        return ans
        


