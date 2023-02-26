# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        d = dummy = ListNode()
        
        while head:
            if head.val not in s:
                d.next = ListNode(head.val)
                d = d.next
                s.add(head.val)
            head = head.next
            
        print(d)
        return dummy.next
