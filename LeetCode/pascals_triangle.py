# 118: Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1: return []
        tri = [[1]]

        while len(tri) < numRows:
            last = tri[-1]
            newLevel = [1]

            for idx in range(len(last)-1):
                if last[idx+1]: newLevel.append(last[idx] + last[idx+1])
            
            newLevel.append(1)
            tri.append(newLevel)
        
        return tri