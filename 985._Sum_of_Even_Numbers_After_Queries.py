class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        esum = 0
        for x in nums:
            if not x % 2:
                esum += x
        print(esum)
        
        res = []
        for i in range(len(queries)):
            val , idx = queries[i]
            # print("before: ", nums, esum)
            tmp = nums[idx]
            nums[idx] += val
            if not nums[idx] % 2:
                esum += nums[idx]
            if not tmp % 2:
                esum -= tmp
            
            
            # print("after: ", nums, esum)
            res.append(esum)
            # if nums[idx] % 2:
            #     f= res[-1] - nums[idx]
            #     res.append(f)
            #     # esum -= nums[idx]
            # else:
            #     f= res[-1] + nums[idx]
            #     res.append(f)
                # esum += nums[idx]
        # print(res)
        return res
        '''
          
        evens = [8,6,
        [1,2,3,4] [[1,0],[-3,1],[-4,0],[2,3]]
        [2,2,3,4]
        [2,-1,3,4]
        [-2,-1,3,4]
        [-2,-1,3,6]
        '''
