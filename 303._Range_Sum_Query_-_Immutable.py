class NumArray:
​
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pref = list(accumulate(self.nums))
        # print(self.pref)
    def sumRange(self, left: int, right: int) -> int:
        if left:
            return self.pref[right] - self.pref[left-1]
        else:
            return self.pref[right]
​
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
