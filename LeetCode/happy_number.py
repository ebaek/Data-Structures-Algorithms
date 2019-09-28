#202: Happy Number

# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: 
# Starting with any positive integer, replace the number by the 
# sum of the squares of its digits, and repeat the process 
# until the number equals 1 (where it will stay), or it 
# loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.

# Example: 

# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Approach:
# keep recalculating happy number until number is either 1 or 0
# if number is 1: return False
# if number is 0: return True 

# break down the number by % 10 
# square the % 10 number and add to sum


class Solution:
    def isHappy(self, num: int) -> boolean:
            seen = set()
            while num not in seen:
                seen.add(num)
                num = sum([int(ch) ** 2 for ch in str(num)])
            return num == 1
    
