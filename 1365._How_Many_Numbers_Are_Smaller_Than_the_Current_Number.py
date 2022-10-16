class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        
        for i in range(0,len(nums)):
            for j in range(0, len(nums)):                 
                if nums[i] > nums[j]:
                    try:
                        arr[i] +=1
                    except:
                        pass
        return arr
