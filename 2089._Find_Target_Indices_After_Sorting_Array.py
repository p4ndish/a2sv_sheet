class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = sorted(nums)
        
        count = []
        for i in range(len(n)):
​
            if n[i] == target:
                # print(i)
                count.append(i)
            
        return count
