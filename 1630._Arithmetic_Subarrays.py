class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        res = []
        for i in range(len(l)):
            start = l[i]
            end = r[i]
            sub =  sorted(nums[start:end+1])
            # print(sub)
            s = set(sub[j+1]-sub[j] for j in range(len(sub)-1))
            # print(s)
            if len(s) == 1:
                res.append(True)
            else:
                res.append(False)
        # print(res)
        return res
        
        
        
        
        
        
        
'''
       def tt():
            return True
​
        def ff():
            return False
        ll, rr = 0,0
        res = []
        
        while (ll,rr) < (len(l),len(r)):
            sol =[]
            for i in range(l[ll],r[rr]+1):
                sol.append(nums[i])
            # print(sol)
            diff = sol[1] - sol[0]
            n = len(sol)
​
            const = None
            sol.sort()
            v = set([sol[i+1]-sol[i] for i in range(len(sol)-1)])
            if len(v) == 1:
                res.append(tt())
            else:
                res.append(ff())
            ll+=1
            rr+=1
        # print(res)
  
        return res
'''
​
