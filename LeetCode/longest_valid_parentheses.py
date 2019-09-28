# 32: Longest Valid Parentheses

# Given a string containing just the characters '(' and ')', find the length 
# of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"

# Example 2:
# Input: ")()())"
# Output: 4

# current character: )
# stack: (

# Approach: 
# maintain a dictionary with variation of open parentheses as keys pointing
# to variations of closed parentheses as values
# iterate through the string and push to stack the character if it is an open parens
# if not an open parens, then pop the last element off the stack and compare to
# dictionary[closedparens], if the same add 2 to current count
# if ever run into invalid pairing, reset the count to 0

# ")()())"
# stack: 
# current char: 
# count = 2


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxDiff = 0

        for idx in range(len(s)):
            if s[idx] == "(": stack.append(idx)
            else:
                if stack: stack.pop()
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    maxDiff = max(maxDiff, idx - stack[-1])
        return maxDiff
