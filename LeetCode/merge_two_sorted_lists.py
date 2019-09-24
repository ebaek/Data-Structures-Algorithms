# 21: Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.


# Approach:
# 2 pointers pointing to either lists 
# compare the values and make compare point 

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mainHead = cur = ListNode(None)
        
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            
            cur = cur.next
        cur.next = l1 or l2
        return mainHead.next


