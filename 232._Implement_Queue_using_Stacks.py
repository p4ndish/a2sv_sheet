class MyQueue:
​
    def __init__(self):
        self.data = []
​
    def push(self, x: int) -> None:
        return self.data.insert(0,x)
​
    def pop(self) -> int:
        return self.data.pop()        
​
    def peek(self) -> int:
        return self.data[-1]
​
    def empty(self) -> bool:
        if len(self.data) == 0 :
            return True
​
​
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
