# 394: Decode String

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the 
# square brackets is being repeated exactly k times. Note that k is guaranteed 
# to be a positive integer.

# You may assume that the input string is always valid; 
# No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain 
# any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[ ]]", return "accaccacc".
# s = "2[abc] 3[cd]ef", return "abcabccdcdcdef".

# Approach: use a stack to maintain the order of operations
# while iterating through the string, 

# if char is [ then append to the stack the currentCharacter and currentNumber
# if char is ] then pop off the stack and multiple the num by current string and 
# concatenate the popped off character to the string

# if the character is a number: currentNum is int(num) 
# if the character is a string: concatenate the string 

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currentNum, currentStr = 0, "" 
        
        for ch in s:
            if ch == "[":
                stack.append(currentStr)
                stack.append(currentNum)
                currentNum, currentStr = 0, ""
            elif ch == "]":
                num = stack.pop()
                lastStr = stack.pop()
                currentStr = lastStr + (num * currentStr)
            elif ch.isdigit():
                # need to account for case in which there are multiple digits
                currentNum = currentNum*10 + int(ch)
            else:
                currentStr += ch
        
        return currentStr 