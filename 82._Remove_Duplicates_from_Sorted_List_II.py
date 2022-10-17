# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        farr = []
        dummy = ListNode()
        d = dummy
        for i in arr:
            if arr.count(i) == 1:
                d.next = ListNode(i)
                d = d.next
​
        return dummy.next
        #approch 2
#         dummy = ListNode()
#         dummy.next = head
#         prev = dummy
#         curr = head
#         while curr :
#             while curr.next and curr.val == curr.next.val:
#                 curr = curr.next
#             if prev.next == curr:
#                 prev = curr
#                 curr = curr.next
#             else:
#                 prev.next = curr.next
#                 curr = curr.next
#         return dummy.next
                
            
    
