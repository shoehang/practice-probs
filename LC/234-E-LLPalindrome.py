# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        
        while slow:
            # next = slow.next
            # slow.next = prev
            # prev = slow
            # slow = next
            
            slow.next, slow, prev = prev, slow.next, slow
            
        while prev and head:
            if prev.val == head.val:
                prev = prev.next
                head = head.next
            else:
                return False
        return Trues