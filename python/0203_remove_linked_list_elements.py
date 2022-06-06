# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        if head.val == val:
            while head.val == val and head != None:
                head = head.next
                
        if head == None:
            return head
            
        returnHead = head
            
        while head != None:
            if head.next.val == val:
                head.next = head.next.next
            head = head.next
        
        return returnHead
