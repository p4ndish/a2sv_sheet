class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        d = defaultdict(int)
        d[0] = 1
        sums = 0
        arr = []
        for i in nums:
            if i % 2 == 0:
                arr.append(0)
            else:
                arr.append(1)
        # print(arr)
        for i in range(len(arr)):
            sums += arr[i]
            if sums - k in d:
                # print(sums, k)
                res += d[sums-k]
                d[sums] += 1
            else:
                d[sums] += 1
                
        print(res)
        return res
            
            
            
            
        
'''
[2,2,2,1,2,2,1,2,2,2], k = 2
[0,0,0,1,0,0,1,0,0,0]
[0,0,0,0,1,1,1,2,2,2]
'''
