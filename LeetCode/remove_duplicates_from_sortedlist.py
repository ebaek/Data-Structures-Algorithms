
# 83: Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        curr = pointer = head
        
        while pointer:
            if pointer.val == curr.val:
                pointer = pointer.next
            else:
                curr.next = pointer
                curr = curr.next
        
        curr.next = pointer
        return head
    