# 445: Add Two Numbers II

from collections import deque 

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode(None)
        num1, num2 = deque([]), deque([])
        carry = 0 
        
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        
        while l2: 
            num2.append(l2.val)
            l2 = l2.next
        
        totalStack = []
        
        while num1 or num2 or carry:
            num1Val, num2Val = 0, 0
            
            if num1: num1Val = num1.pop()
            if num2: num2Val = num2.pop()
                
            total = num1Val + num2Val + carry
            if total > 9:
                totalStack.append(total % 10)
                carry = 1
            else:
                totalStack.append(total)
                carry = 0
        
        while totalStack:
            nextDigit = totalStack.pop()
            curr.next = ListNode(nextDigit)
            curr = curr.next
        
        return head.next