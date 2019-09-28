# 7: Reverse Integer 

# Approach: maintain a variable that determines if negative or positive
# two variables: number and reversed
# while number is not 0: multiply the reversed number by 10 and add
# module 10 of the number 
# then divide the number by 10

class Solution:
    def reverse(self, x: int) -> int:
        reversed = 0
        positive = 1
        if x < 0: 
            positive = -1
            x = -1 * x
                    
        while x:
            reversed = (reversed * 10) + (x % 10)
            x //= 10
        
        return 0 if reversed > pow(2, 31) else reversed * positive