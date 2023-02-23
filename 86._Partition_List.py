# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = d1 = ListNode()
        gre = d2 = ListNode()
        
        curr = head
        while curr :
            if curr.val < x:
                d1.next = curr
                d1 = d1.next
                # print(less)
            else:
                d2.next = curr
                d2 = d2.next
            curr = curr.next
        d2.next = None
        d1.next = gre.next
        return less.next
        print(less)
        print(gre)
        
