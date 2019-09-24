# 443: String Compression

# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.

# Follow up:
# Could you solve it using only O(1) extra space?


# Approach:
# Two pointers, one for anchor (current character), the other for keeping track of char occurrences
# If element at second pointer is the same as the element at the first character, keep traversing and increment count 
# At the end, return string compressed 

class Solution(object):
    def compress(self, chars: List[int]):
        if len(chars) == 0 or len(chars) == 1: return len(chars)
        
        idx = 0
        
        while idx < len(chars)-1:
            count = 1
            while idx < len(chars)-1 and chars[idx] == chars[idx+1]:
                count += 1
                del chars[idx]
                
            if count > 1:
                count = str(count)
                charLength = len(count)
                
                for j in range(charLength):
                    chars.insert(idx+1+j, count[j])
                                        
                idx += charLength+1
            else:
                idx += 1
                
        return len(chars)

                




