                            d1.next = prev
                            d1 = d1.next
                            prev = prev.next
                        d1.next = curr
                        d1 = d1.next
                        # print("printing: ", prev)
                        # print("Node: ", dummy)
                        # L += 1
                        curr = curr.next
                    else:
                        d1.next = curr
                        d1 = d1.next
                        curr = curr.next
            L += 1
                
        # print(d1,prev, dummy)
        if prev:
            while prev:
                d1.next = prev
                d1 = d1.next
                prev = prev.next
        # print(curr)
        # print("\n", dummy)
        return dummy.next
