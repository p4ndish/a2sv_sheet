# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        #step 1 
        prev = head
        curr = head.next
        while curr:
            if prev.val == curr.val or prev.val-1000 == curr.val:
                prev.val += 1000
                curr.val += 1000
            prev = prev.next
            curr = curr.next
            
        #step 2 
        
        while head and head.val > 100:
            head = head.next
        
        if not head:
            return head
        
        #step 3 
        cur = head
        while cur and cur.next:
            if cur.next.val > 100:
                cur.next = cur.next.next
            else:
                cur = cur.next
                
