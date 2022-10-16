class MinStack:
​
    def __init__(self):
        self.data = []
        self.minv =[]
    def push(self, val: int) -> None:
        self.minv.append(val)
        
        self.data.append(val)
​
    def pop(self) -> None:
        
        self.minv.pop()
            
        self.data.pop()
​
    def top(self) -> int:
        return self.data[-1]
​
    def getMin(self) -> int:
        return min(self.data) 
​
​
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
