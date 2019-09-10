# 310
# Minimum Height Trees
# Medium


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [set() for _ in range(n)]

        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [idx for idx in range(n) if len(adj[idx]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for idx in leaves:
                j = adj[idx].pop()
                adj[j].remove(idx)
                if len(adj[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves
