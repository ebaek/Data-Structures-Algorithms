# 1047: Remove All Adjacent Duplicates In String
# Time Complexity: O(n)

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        
        for idx in range(len(S)):
            currEl = S[idx]
            if stack and currEl == stack[-1]:
                stack.pop()
            else:
                stack.append(currEl)
        
        return "".join(stack)

# Time Limit Exceeded 
# O(n*m)
class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        idx = 0
        cycle = False
        
        while not cycle:
            if idx == len(S)-1 or not S: 
                break
                
            if S[idx] == S[idx+1]:
                S = S[0:idx] + S[idx+2:]
                idx = 0
                cycle = False
            else: 
                idx += 1
        
        
        return S