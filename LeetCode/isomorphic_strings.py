# 205: Isomorphic Strings

# Approach: 
# make s, t, and key sets and compare their lengths to see 
# if there is a 1:1 ratio for characters 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lenS = len(set(s))
        lenT = len(set(t))
        
        return lenS == len(set(zip(s, t))) == lenT
        

        