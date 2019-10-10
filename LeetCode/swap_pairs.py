# 24: Swap Nodes in Pairs

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Iterative approach
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(0)
        dummy.next = head
        
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            prev.next = tmp
            prev = head
            head = head.next
        
        return dummy.next

# Recursive Approach
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        
        return second
