# 3: Largest Prime

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def largestPrime(n):
    memo = {}
    def isPrime(n):
        for fac in range(2, n):
            if n % fac == 0: return False
        return True
    
    num = n//2
    
    while num > 1:
        if n % num == 0 and isPrime(num): return num
        num -= 1
    
    return None
            
        
a = largestPrime(600851475143)
print(a)
