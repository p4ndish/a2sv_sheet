# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        #approch two
​
        # slow,fast = head,head.next
        # while fast:
        #     slow = slow.next
        #     if fast.next:
        #         fast = fast.next.next
        #     else:
        #         fast = None
        # return slow
        
        
    
#         node = ListNode()
#         n = node
#         s = 0
#         curr = head
#         while curr:
#             curr = curr.next
#             s+=1
#         mid = s//2
#         cur = head
#         res = []
#         while cur:
#             if mid > 0:
#                 mid-=1
#             else:
