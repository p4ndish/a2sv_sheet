class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        #sort them
        s = sorted(map(int,nums), reverse=True)
        print(s)
        k= k-1
        i = len(nums)-1
​
        # print(s[k])
        return str(s[k])
