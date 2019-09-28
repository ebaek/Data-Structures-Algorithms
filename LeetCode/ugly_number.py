# 263: Ugly Number

# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

# Example 1:
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
# Example 3:

# Input: 14
# 3 Output: false 
# Explanation: 14 is not ugly since it includes another prime factor 7.

# [2,3,5]
# 6 
# is div by 2 => 3, [2] => is div by 3 => 1, [1,3]
# 

# Approach:
# iterate through 2, 3, 5 and recursively call isUglyHelper on the number if perfectly divisible
# once hit the base case then append to allCombos

# Time Complexity: O(n) 
# Space Complexity: O(1)

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0: return False
        if(num == 1): return True

        for fac in [2, 3, 5]:
            if num % fac == 0:
                if self.isUgly(num//fac):
                    return True

        return False


