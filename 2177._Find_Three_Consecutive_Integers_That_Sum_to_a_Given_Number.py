class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        cnt = 0
        if num % 3:
            return []
        return [num//3-1,num//3,num//3+1]
        
