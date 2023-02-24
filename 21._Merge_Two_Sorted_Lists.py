# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
​
        prev = None 
        d = dummy = ListNode()
        while p1 and p2:
            if p1.val < p2.val:
                d.next = p1
                d = d.next
                p1 = p1.next
            else:
                d.next = p2
                d = d.next
                p2 = p2.next
        
        if p1:
            d.next = p1
            d = d.next
        elif p2:
            d.next = p2
            d = d.next
        # print(dummy)
        return dummy.next
        
                
                
                
