# 92: Reverse Linked List II 

# Approach: very similar to reversed linked list 1 but keep track of start, end, prev, curr

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        
        for _ in range(m-1):
            start = start.next
        
        # why do we set to start.next
        end = curr = start.next
        
        prev = None
        
        for _ in range(n-m+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        start.next = prev
        end.next = curr
        
        return dummy.next