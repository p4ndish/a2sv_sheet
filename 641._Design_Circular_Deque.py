        if not self.isEmpty():
            return self.qeue[0]
        return -1
​
    def getRear(self) -> int:
        if not self.isEmpty():
            return self.qeue[-1]
        return -1
​
    def isEmpty(self) -> bool:
        if self.length == 0:
            return True
        return False
​
    def isFull(self) -> bool:
        if self.length == self.k :
            return True
        return False
​
​
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
