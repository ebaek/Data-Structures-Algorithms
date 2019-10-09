# 6: ZigZag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        fullStr = [ [] for _ in range(numRows)]
        
        cycleIdx, up = 0, True
        
        for idx in range(len(s)):
            if cycleIdx == 0: up = True
            if cycleIdx == numRows-1: up = False
            
            fullStr[cycleIdx].append(s[idx])
            
            if up:
                cycleIdx += 1
            else:
                cycleIdx -= 1
        
        converted = ""
        for series in fullStr:
            converted += "".join(series)
        
        return converted
    