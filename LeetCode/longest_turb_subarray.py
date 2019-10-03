class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if not A: return 0
        maxLength = 1
        anchor = 0
        
        def compare(el1, el2):
            if el1 < el2:
                return -1
            elif el1 > el2:
                return 1
            else:
                return 0
        
        for idx in range(1, len(A)):
            comp = compare(A[idx-1], A[idx])
            
            if comp == 0:
                anchor = idx
            elif idx == len(A)-1 or comp*compare(A[idx], A[idx+1]) != -1:
                maxLength = max(maxLength, idx-anchor+1)
                anchor = idx
        
        return maxLength