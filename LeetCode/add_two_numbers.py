class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        pointer = head
        carry = 0
        
        while l1 or l2 or carry:            
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            pointer.next = ListNode(carry % 10)
            pointer = pointer.next
            carry //= 10

        return head.next
            