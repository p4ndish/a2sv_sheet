# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # n -= 1 
        fast, slow = head, head
        cnt = 0
        scnt = 0 
        d = dummy = ListNode()
        while fast:
            fast = fast.next
            cnt += 1
        # print(cnt)
        i = 0 
        while slow and cnt - i != n :
            d.next = slow
            d = d.next
            slow = slow.next
            i += 1
        # print(slow)
        if slow:
            d.next = slow.next
            d = d.next
        return dummy.next
