class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        left = []
        right = []
        same = []
        
        
        for i in nums:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                same.append(i)
        return left + same + right
        
        
        
        '''
        [9,12,5,10,14,3,10] 10
        9 5 3 
        10 10
        
        '''
