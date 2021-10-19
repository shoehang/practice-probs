# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        s1 = []
        s2 = []
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        
        node = None
        
        while s1 or s2 or carry:
            val1 = s1.pop() if s1 else 0
            val2 = s2.pop() if s2 else 0
            
            curr = val1 + val2 + carry
            carry = curr // 10
            newVal = curr % 10
            
            new_node = ListNode(newVal)
            new_node.next = node
            node = new_node
            
        return node