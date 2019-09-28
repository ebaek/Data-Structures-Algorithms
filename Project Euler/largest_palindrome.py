# 4: Largest palindrome product

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers 
# is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def palindromicProduct():
    # all three digit palindromes 
    pals = allPalindromes()
    pals.sort(reverse=True)
        
    for idx1 in range(len(pals)):
        for idx2 in range(idx1+1, len(pals)):
            prod = pals[idx1] * pals[idx2]
            if isPalindrome(prod): return prod 

    return None
            
def isPalindrome(num):
    toStr =str(num)
    start, end = 0, len(toStr)-1
    
    while start < end: 
        if toStr[start] != toStr[end]: return False 
    
    return True 

def allPalindromes():
    allPals = []
    
    for mid in range(0,10):
        for end in range(0,10):
            strNum = str(end) + str(mid) + str(end)
            allPals.append(int(strNum))
    
    return allPals


a = palindromicProduct()
print(a)

