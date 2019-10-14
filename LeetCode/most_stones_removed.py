# 947: Most Stones Removed with Same Row or Column

# Union find method 
class Solution(object):
    def removeStones(self, stones):
        X, Y = {}, {}
        union_find = [idx for idx in range(len(stones))]
        
        # FIND 
        def find(x):
            if x != union_find[x]: union_find[x] = find(union_find[x])
            return union_find[x]
        
        for idx, coord in enumerate(stones):
            x, y = coord
            
            if x not in X: X[x] = idx
            if y not in Y: Y[y] = idx
            
            # UNION 
            # group together stones that share the same x/ y coordinate
            union_find[find(Y[y])] = find(idx)
            union_find[find(X[x])] = find(idx)
        
        # return the difference between the number of stones, and the number of islands
        return len(stones) - len(set([find(idx) for idx in range(len(stones))]))