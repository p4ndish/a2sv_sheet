class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        c = {nums[i]:i for i in range(len(nums))}
        # print(c)
        for n in operations:
            re,val = n
            # print(re,val)
            if re in c:
                nums[c[re]] = val
                c[nums[c[re]]] = c[re]
                del c[re] 
            # print(nums)
                
        print(nums)
        return nums
        
        
'''
[1,2,4,6]
[[1,3],[4,7],[6,1]]
​
1:0
2:1
4:2
6:3
​
​
'''
