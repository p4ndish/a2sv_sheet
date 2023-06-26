        
        
        left = head
        mid = self.get_mid(head)
        right = mid.next
        mid.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        
        
        return self.merge(left, right)
        
        
    def merge(self, l, r):
        d = dummy = ListNode()
        left = l
        right = r
        while left and right:
            if left.val < right.val:
                d.next = left
                left = left.next
            else:
                d.next = right
                right = right.next
            d = d.next
​
        if left: d.next = left
        if right: d.next = right
            
        return dummy.next
