class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def rev(s):
            s=  str(s)[::-1]
            # print(s)
            return s.lstrip('0')
            # pass
        N = len(nums)
        num = []
        for n in nums:
            a = rev(n)
            num.append(int(a))
        # print(num)
        nums += num
        # print(nums)
        return len(set(nums))
