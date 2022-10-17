class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         c = Counter(nums)
#         s = [x[0] for x in sorted(c.items(), key=lambda x: -x[1])]
#         return s[0:k]
            
        heapq._heapify_max(nums)
        res = []
        for i in range(k):
            res.append(heapq._heappop_max(nums))
        print(res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(nums) == 1:
​
#             return nums
#         else:
#             # count = [0]*(max(nums)+1)
#             res = []
#             from collections import Counter
#             s = Counter(nums)
#             values = list(map(list,s.most_common(k)))
#             for i in values:
                
#                 res.append(i[0])
#             return res
            
