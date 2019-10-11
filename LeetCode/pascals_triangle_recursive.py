# 118: Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        
        lastRows = self.generate(numRows-1)
        rows = []
        
        for idx in range(numRows):
            if idx == 0 or idx == numRows-1: rows.append(1)
            else: 
                rows.append(lastRows[-1][idx-1] + lastRows[-1][idx])
        
        lastRows.append(rows)
        return lastRows
    
# 119: Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]

        lastRow = self.getRow(rowIndex-1)

        for idx in range(len(lastRow)-1):
            lastRow[idx] = lastRow[idx] + lastRow[idx+1]

        return [1] + lastRow
