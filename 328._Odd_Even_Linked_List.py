    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None or head.next.next==None:
            return head
        t1=head
        temp=t2=head.next
        while t2.next and t2.next.next:
            t1.next=t2.next
            t2.next=t2.next.next
            t1=t1.next
            t2=t2.next            
        if t2.next:
            t1.next=t2.next
            t2.next=None
            t1=t1.next
        t1.next=temp
        return head 
        
        
#         curr = head
#         slow = head.next
#         fast = head.next.next
​
        
#         while fast and fast.next:
#             tmp = slow.val
#             slow.val = fast.val
#             fast.val = tmp
#             slow = slow.next
#             fast = fast.next.next
#         print(fast)
#         print(slow)
#         tmp = fast.val
#         while slow:
#             print("changing: ", slow.val, f"to: {tmp}")
#             s = slow.val
#             slow.val = tmp
#             tmp = s 
#             slow = slow.next
#         print(slow)
#         return head
#         # while slow.next:
#         #     if slow.next.next and slow.next.next == None:
#         #         tmp = slow.val
#         #         slow.val = slow.next.val
#         #         slow.next.val = tmp
#         #     slow = slow.next
​
#         print(slow)
#         print(head)
        
