# 390: Elimination Game

# There is a list of sorted integers from 1 to n. Starting from left to right, 
# remove the first number and every other number afterward until you reach 
# the end of the list.

# Repeat the previous step again, but this time from right to left, 
# remove the right most number and every other number from the 
# remaining numbers.

# We keep repeating the steps again, alternating left to right and 
# right to left, until a single number remains.

# Find the last number that remains starting with a list of length n.

# Example:
# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6

class Solution(object):
    def lastRemaining(self, n):
        head = 1
        steps = 1
        remaining = n
        leftToRight = True

        while remaining > 1:
            if leftToRight or remaining % 2 == 1:
                head += steps

            steps *= 2
            remaining //= 2
            if leftToRight:
                leftToRight = False
            else:
                leftToRight = True

        return head
