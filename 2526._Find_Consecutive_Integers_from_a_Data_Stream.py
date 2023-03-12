class DataStream:
​
    def __init__(self, value: int, k: int):
        self.arr = []
        self.value = value
        self.k = k 
        self.cont = 0
        self.length = 0 
    def consec(self, num: int) -> bool:
        self.arr.append(num)
        self.length += 1 
        if self.value == num:
            self.cont += 1 
        else:
            self.cont = 0 
        if self.length < self.k:
            return False
        if self.k <= self.cont:
            return True
        
​
​
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
