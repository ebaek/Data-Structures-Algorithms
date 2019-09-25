# 148: Sort List

# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Approach: merge sort is the most appropriate because can insert nodes in O(1) time, so complexity would be O(nlogn)
# Quicksort would be slower because LinkedLists do not have random access to nodes


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        otherHalf = slow.next

        slow.next = None

        left = self.sortList(head)
        right = self.sortList(otherHalf)

        def merge(left, right):
            if not left or not right:
                return left or right
            if left.val > right.val:
                left, right = right, left

            head = prev = left
            left = left.next

            while left and right:
                if left.val <= right.val:
                    prev.next = left
                    left = left.next
                else:
                    prev.next = right
                    right = right.next
                prev = prev.next

            prev.next = left or right
            return head

        return merge(left, right)
            
                
                
        
        
        
        
        
