# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr == arr[::-1]
        # #reverse it then check it
        # prev=ListNode()
        # curr = head
        # while curr:
        #     tmp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = tmp
        # new_curr = head
        # print(prev)
        # while prev.next or new_curr:
        #     if new_curr.val != prev.val:
        #         return False
        #     new_curr = new_curr.next
        #     prev = prev.next
        # return True
