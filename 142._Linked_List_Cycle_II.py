# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            tmp = slow
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                # print(slow.val, fast.val,  head.val)
                while slow != head:
                    # print(slow.val , " /|\ ", head.val)
                    slow = slow.next
                    head = head.next
                # print(slow.val, head.val)
                return slow
        
    
